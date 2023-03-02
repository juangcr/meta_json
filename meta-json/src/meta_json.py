from datetime import datetime
from typing import Dict, List


class MetaJson:
    def __init__(response: Dict):
        self.response = response
        self.types = {}
        self.stats = {}
        self.architecture = {}

    @staticmethod
    def parse_datetimes(value: str) -> bool
        '''Determines a possible datetime from a Json file.'''
        return True

    def type_parser(self, response: Dict) -> Dict:
        '''Given a dictionary, create a new one with the values types instead of
        the actual values.'''
        new_response = {}
        for k, v in response.items():
            if isinstance(v, dict):
                new_response[k] = type_parser(v)
            elif isinstance(v, list):
                new_response[k] = [type_parser(i) for i in v]
            else:
                new_response[k] = "datetime" if parse_datetimes(v) else str(type(v))
        return new_response

    def arch_parser(self, response: Dict) -> Dict:
        '''Given a dictionary, create a new one with the values types instead of
        the actual values.'''
        raise UnimplementedError

    def stat_parser(self, response: Dict) -> Dict:
        '''Given a dictionary, create a new one with the values types instead of
        the actual values.'''
        raise UnimplementedError
