from typing import Dict, List, Union
from meta_json.meta_json_parser import MetaJsonParser


class MetaJson:
    """MetaJson main module."""

    def __init__(self, response: Union[Dict, List]):
        """Run all parsers in constructor."""

        self.response = response
        self.__parser = MetaJsonParser()

    def attributes(self):
        """Return attributes result."""
        return self.__parser.attribute_parser(self.response)

    def layers(self):
        """Return layers result."""
        layers = self.__parser.layer_processing(
            self.__parser.layer_parser(self.response)
        )
        return self.__parser.layers_retrieval(layers)

    def types(self):
        """Return types result."""
        return self.__parser.types_parser(self.response)
