from typing import Dict. List, Union
from src.meta_json.meta_json_parser import MetaJsonParser


class MetaJson:
    def __init__(self, response: Union[Dict, List]):
        parser = MetaJsonParser()
        self.__types = parser.types_parser(response)
        self.__structure = parser.structure_parser(response)

    def types(self):
        return self.__types

    def structure(self):
        return self.__structure
