import pytest
from src.meta_json.meta_json import MetaJson


def test_meta_json_empty():
    meta = MetaJson({})
    assert meta.types == {}
    assert meta.attributes == [[], []]
    assert meta.layers == {}
