import pytest
from src.meta_json.meta_json_parser import MetaJsonParser

def test_metadata_json():
    meta = MetaJsonParser()
    assert True


def test_meta_json_datetimes():
    data = [
	    "2014-12-09T13:50:51.644000Z",
	    "2014-12-20T21:17:56.891000Z",
	    "https://swapi.dev/api/people/1/"
        ]

    meta = MetaJsonParser()
    assert meta._parse_datetimes(data[0]) == True
    assert meta._parse_datetimes(data[1]) == True
    assert meta._parse_datetimes(data[2]) == False


def test_meta_json_flat_list():
    input_data = [
	    "item_1",
	    "item_2",
	    ["item_3", "item_4", "item_5"],
	    ["item_6"]
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


def test_meta_json_types():
    input_data = {
		"name": "Luke Skywalker",
		"height": 1.72,
		"mass": 77,
		"hair_color": "blond",
		"skin_color": "fair",
		"eye_color": "blue",
		"birth_year": "19BBY",
		"gender": "male",
		"homeworld": "https://swapi.dev/api/planets/1/",
		"films": [
			"https://swapi.dev/api/films/2/",
			"https://swapi.dev/api/films/6/",
			"https://swapi.dev/api/films/3/",
			"https://swapi.dev/api/films/1/",
			"https://swapi.dev/api/films/7/"
	    ],
		"species": [
			"https://swapi.dev/api/species/1/"
    	],
		"vehicles": [
			"https://swapi.dev/api/vehicles/14/",
			"https://swapi.dev/api/vehicles/30/"
	    ],
		"starships": [
			"https://swapi.dev/api/starships/12/",
			"https://swapi.dev/api/starships/22/"
    	],
		"created": "2014-12-09T13:50:51.644000Z",
		"edited": "2014-12-20T21:17:56.891000Z",
		"url": "https://swapi.dev/api/people/1/"
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
	    "homeworld": "str",
	    "films": [
		    "str",
		    "str",
		    "str",
		    "str",
		    "str"
	    ],
	    "species": [
	        "str"	
	    ],
	    "vehicles": [
	        "str",
	        "str"
	    ],
	    "starships": [
	        "str",
	        "str"
	    ],
    	"created": "datetime",
	    "edited": "datetime",
    	"url": "str" 
    }

    meta = MetaJsonParser()
    meta_types = meta.types_parser(input_data)
    assert meta_types == output_data

def test_meta_json_structure():
    input_data = {
		"name": "Luke Skywalker",
		"height": 1.72,
		"mass": 77,
		"hair_color": "blond",
		"skin_color": "fair",
		"eye_color": "blue",
		"birth_year": "19BBY",
		"gender": "male",
		"homeworld": "https://swapi.dev/api/planets/1/",
		"films": [
			"https://swapi.dev/api/films/2/",
			"https://swapi.dev/api/films/6/",
			"https://swapi.dev/api/films/3/",
			"https://swapi.dev/api/films/1/",
			"https://swapi.dev/api/films/7/"
	    ],
		"species": [
			"https://swapi.dev/api/species/1/"
    	],
		"vehicles": [
			"https://swapi.dev/api/vehicles/14/",
			"https://swapi.dev/api/vehicles/30/"
	    ],
		"starships": [
			"https://swapi.dev/api/starships/12/",
			"https://swapi.dev/api/starships/22/"
    	],
		"created": "2014-12-09T13:50:51.644000Z",
		"edited": "2014-12-20T21:17:56.891000Z",
		"url": "https://swapi.dev/api/people/1/"
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
	    "homeworld",
	    "films",
	    "species",
	    "vehicles",
	    "starships",
    	"created",
	    "edited",
    	"url" 
        ], []]
    meta = MetaJsonParser()
    meta_types = meta.structure_parser(input_data)
    assert meta_types == output_data

