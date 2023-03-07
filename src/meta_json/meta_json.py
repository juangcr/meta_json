from typing import Dict, List, Any


class MetaJson:
    def __init__(self, response: Dict):
        self.response = response
        self.types: Dict = {}
        self.stats: Dict = {}
        self.structure: Dict = {}

    @staticmethod
    def parse_datetimes(value: str) -> bool:
        """Determines a possible datetime from a Json file."""
        return True

    @staticmethod
    def list_flattener(vals: List) -> List:
        """"""
        new_list = []
        for val in vals:
            if isinstance(val, list):
                new_list.extend(val)
            else:
                new_list.append(val)
        return new_list

    def type_parser(self, response: Dict) -> Dict:
        """Given a dictionary, create a new one with the values types instead
        of the actual values."""
        new_response: Dict[Any, Any] = {}
        for k, v in response.items():
            if isinstance(v, dict):
                new_response[k] = self.type_parser(v)
            elif isinstance(v, list):
                new_response[k] = [self.type_parser(i) for i in v]
            else:
                new_response[k] = (
                    "datetime" if self.parse_datetimes(v) else str(type(v))
                )
        return new_response

    def arch_parser(self, response: Dict) -> Dict:
        """Given a dictionary, create a one describing the JSON model instead
        of the actual values."""
        raise NotImplementedError

    def stat_parser(self, response: Dict) -> Dict:
        """Given a dictionary, create a new one with the descriptive statistics
        instead of the actual values."""
        raise NotImplementedError
