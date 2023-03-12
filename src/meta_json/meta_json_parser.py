import re
from typing import Dict, List, Any, Union


class MetaJsonParser:
    """MetaJson parsing utilities."""

    @staticmethod
    def _parse_datetimes(value: str) -> bool:
        """Determine if a string is a potential datetime.

        Attributes
        ----------
        value: str
            Variable to evaluate.

        Returns
        -------
        bool
            True if a datetime, false otherwise.
        """
        rgx = re.compile(r"\d{4}\-[0-1]\d\-[0-3]\d")
        return bool(re.match(rgx, value))

    def _list_flattener(self, vals: List) -> List:
        """Chain nested lists into a new one.

        Attributes
        ----------
        vals: list
            List with nested lists.

        Returns
        -------
        list
            List with all previous nested values.
        """
        new_list = []
        for val in vals:
            if isinstance(val, list):
                new_list.extend(self._list_flattener(val))
            else:
                new_list.append(val)
        return new_list

    def _soft_flatten(self, vals: List) -> List:
        """Turn double braces into one.

        Attributes
        ----------
        vals: list
            List with nested lists.

        Returns
        -------
        list
            List with reduced braces.
        """
        new_list = []
        for val in vals:
            if not isinstance(val, list):
                new_list.append(val)
            else:
                new_list.extend(val)
        return new_list

    def types_parser(self, response: Any) -> Union[Union[Dict, List], str]:
        """Given a JSON response, create a dictionary with the value types
        instead of the actual values.

        Attributes
        ----------
        response:
            Deserialized JSON response, could be total or partial.

        Return
        -------
        list, dict, str
            Same response but with data types instead of values.
        """
        if isinstance(response, dict):
            return {k: self.types_parser(v) for k, v in response.items()}
        elif isinstance(response, list):
            return [self.types_parser(r) for r in response]
        else:
            if self._parse_datetimes(str(response)):
                return "datetime"
            return re.sub("(<class '|'>)", "", str(type(response)))

    def attribute_parser(self, response: Any) -> List:
        """Given a JSON response, create a list grouping its attributes.

        Attributes
        ----------
        response:
            Deserialized JSON response, could be total or partial.

        Returns
        -------
        list
            List with grouped keys lists [primary keys, subkeys].
        """
        # fmt: off
        if isinstance(response, dict):
            return [list(response.keys()),
                    self.attribute_parser(list(response.values()))]
        elif isinstance(response, list):
            return self._list_flattener(
                    [self.attribute_parser(r) for r in response])
        else:
            return []
        # fmt: on

    def layer_parser(self, response: Any) -> List:
        """Given a JSON response, create a list showing attributes'
        depth per layer.

        Attributes
        ----------
        response:
            Deserialized JSON response, could be total or partial.

        Returns
        -------
        list
            List with key pairs [key, [subkeys]].
        """
        if isinstance(response, dict):
            return [[k, self.layer_parser(v)] for k, v in response.items()]
        elif isinstance(response, list):
            return self._soft_flatten([self.layer_parser(r) for r in response])
        else:
            return []

    def layer_processing(self, parsed_layer: List) -> List:
        """Create a list with sorted attribute layers from a previously parsed
        response into layers.

        Attributes
        ----------
        parsed_layer: list
            Result from layer_parser method.

        Returns
        -------
        list
            List with grouped attributes per layer [[layer1], [layer2]...].
        """
        layers = []
        while len(parsed_layer) > 0:
            layers.append([p.pop(0) for p in parsed_layer if len(p) > 0])
            bring_next = [p[0] for p in parsed_layer if len(p) > 0]
            filtered_layer = [*filter(lambda x: x != [], bring_next)]
            parsed_layer = self._soft_flatten(filtered_layer)
        return layers

    @staticmethod
    def layers_retrieval(processed_layer: List) -> Dict:
        """Create a dictionary with the processed attribute layers.

        Attributes
        ----------
        processed_layer: list
            Result from layer_processing method.

        Returns
        -------
        dict
            Dictionary with attributes per layer {"layer_0": [attributes],...}.
        """
        return {f"layer_{idx}": val for idx, val in enumerate(processed_layer)}
