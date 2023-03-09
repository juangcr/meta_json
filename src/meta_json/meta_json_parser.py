import re
from typing import Dict, List, Any, Union


class MetaJsonParser:
    """MetaJson parsing utilities."""

    @staticmethod
    def _parse_datetimes(value: Any) -> bool:
        """Determine if a string is a potential datetime."""
        rgx = re.compile(r"\d{4}\-[0-1]\d\-[0-3]\d")
        return bool(re.match(rgx, str(value)))

    def _list_flattener(self, vals: List) -> List:
        """Chain nested lists into a new one."""
        new_list = []
        for val in vals:
            if isinstance(val, list):
                new_list.extend(self._list_flattener(val))
            else:
                new_list.append(val)
        return new_list

    def types_parser(self, response: Any) -> Union[Union[Dict, List], str]:
        """Given a JSON response, create a dictionary with the value types
        instead of the actual values."""
        if isinstance(response, dict):
            return {k: self.types_parser(v) for k, v in response.items()}
        elif isinstance(response, list):
            return [self.types_parser(r) for r in response]
        else:
            if self._parse_datetimes(response):
                return "datetime"
            return re.sub("(<class '|'>)", "", str(type(response)))

    def attribute_parser(self, response: Any) -> List:
        """Given a JSON response, create a list grouping its attributes."""
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

    def tree_parser(self, response: Any) -> Dict:
        """Given a JSON response, create a dictionary showing attributes
        per depth layer."""
        raise NotImplementedError
