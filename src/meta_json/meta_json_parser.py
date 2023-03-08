import re
from typing import Dict, List, Any, Union, Optional


class MetaJsonParser:
    """MetaJson parsing utilities."""

    @staticmethod
    def _parse_datetimes(value: Any) -> bool:
        """Determine if a string is a potential datetime."""
        return bool(re.match(r"\d{4}\-(0|1)\d\-[0-3]\d", str(value)))

    @staticmethod
    def _list_flattener(vals: List) -> List:
        """Chain nested lists into a new one."""
        new_list = []
        for val in vals:
            if isinstance(val, list):
                new_list.extend(val)
            else:
                new_list.append(val)
        return new_list

    def types_parser(self, response: Any) -> Union[Union[Dict, List], str]:
        """Given a JSON response, create a new one with the value types instead
        of the actual values."""
        if isinstance(response, dict):
            return {k: self.types_parser(v) for k, v in response.items()}
        elif isinstance(response, list):
            return [self.types_parser(r) for r in response]
        else:
            if self._parse_datetimes(response):
                return "datetime"
            return str(type(response)).replace("<class '", "").replace("'>", "")

    def structure_parser(self, response: Any) -> Optional[List]:
        """Given a JSON response, create a one describing its model instead."""
        if isinstance(response, dict):
            return [
                    list(response.keys()),
                    [self.structure_parser(i) for i in response.values()] 
                    ]
        elif isinstance(response, list):
            return [self.structure_parser(r) for r in response]
        # else:
            # continue

