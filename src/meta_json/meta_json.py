from typing import Dict, List, Union
from meta_json.meta_json_parser import MetaJsonParser


class MetaJson:
    def __init__(self, response: Union[Dict, List]):
        parser = MetaJsonParser()
        self.__types = parser.types_parser(response)
        self.__attributes = parser.attribute_parser(response)
        layers = parser.layer_processing(parser.layer_parser(response))
        self.__layers = parser.layers_retrieval(layers)

    def types(self):
        return self.__types

    def attributes(self):
        return self.__attributes

    def layers(self):
        return self.__layers
