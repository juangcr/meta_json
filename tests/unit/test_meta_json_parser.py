import pytest
from src.meta_json.meta_json_parser import MetaJsonParser

def test_metadata_json():
    meta = MetaJsonParser()
    assert True


def test_meta_json_datetimes():
    data = [
	    "2014-12-09T13:50:51.644000Z",
	    "2014-12-20T21:17:56.891000Z",
	    "https://api.dev/api/1/"
        ]

    meta = MetaJsonParser()
    results = [meta._parse_datetimes(d) for d in data]
    assert results == [True, True, False] 


def test_meta_json_flat_list():
    input_data = [
	    "item_1",
	    "item_2",
	    ["item_3", "item_4", "item_5"],
	    ["item_6"],
	    [],
	    [[], []]
        ]

    output_data = [
	    "item_1",
	    "item_2",
	    "item_3",
	    "item_4",
	    "item_5",
	    "item_6"
        ]

    meta = MetaJsonParser()
    result = meta._list_flattener(input_data)
    assert result == output_data 


def test_meta_json_types_one_layer():
    input_data = {
		"name": "John Doe",
		"height": 1.73,
		"mass": 77,
		"hair_color": "blond",
		"skin_color": "fair",
		"eye_color": "blue",
		"birth_year": "1970",
		"gender": "male",
		"species": ["Human"],
		"created": "2023-03-09T13:50:41.674000Z",
		"edited": "2023-03-20T21:17:53.791000Z",
		"url": "https://www.url.dev"
    }

    output_data = {
		"name": "str",
	    "height": "float",
	    "mass": "int",
	    "hair_color": "str",
	    "skin_color": "str",
	    "eye_color": "str",
	    "birth_year": "str",
	    "gender": "str",
	    "species": ["str"],
    	"created": "datetime",
	    "edited": "datetime",
    	"url": "str" 
    }

    meta = MetaJsonParser()
    meta_types = meta.types_parser(input_data)
    assert meta_types == output_data

def test_meta_json_attribute_one_layer():
    input_data = {
		"name": "John Doe",
		"height": 1.73,
		"mass": 77,
		"hair_color": "blond",
		"skin_color": "fair",
		"eye_color": "blue",
		"birth_year": "1970",
		"gender": "male",
		"species": ["Human"],
		"created": "2023-03-09T13:50:41.674000Z",
		"edited": "2023-03-20T21:17:53.791000Z",
		"url": "https://www.url.dev"
    }

    output_data = [[
		"name",
	    "height",
	    "mass",
	    "hair_color",
	    "skin_color",
	    "eye_color",
	    "birth_year",
	    "gender",
	    "species",
    	"created",
	    "edited",
    	"url" 
        ], []]
    meta = MetaJsonParser()
    meta_attr = meta.attribute_parser(input_data)
    assert meta_attr == output_data


def test_meta_json_attributes_multiple_layers():
    input_data = {
            "layer1_a": "text",
            "layer1_b": 3.14,
            "layer1_c": {
                "layer2_a": 42,
                "layer2_b": "more text"
                },
            "layer1_d": ["bit", "more", "text"],
            "layer1_e": {
                "layer2_c": [
                    {"layer3_a": "deep"},
                    {"layer3_b": "deeper"}
                    ],
                "layer2_d": {
                    "layer3_c": {"layer4_a": "deepest"}
                    }
                }
            }

    output_data = [
            [
                "layer1_a",
                "layer1_b",
                "layer1_c",
                "layer1_d",
                "layer1_e",
                ],
            [
                'layer2_a',
                'layer2_b',
                'layer2_c',
                'layer2_d',
                'layer3_a',
                'layer3_b',
                'layer3_c',
                'layer4_a'
                ]
            ]

    meta = MetaJsonParser()
    meta_attr = meta.attribute_parser(input_data)
    assert meta_attr == output_data
