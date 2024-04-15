import pytest
import json
import os
from timeit import default_timer
from meta_json import MetaJson

def test_integration():
    """Read the TESTING.md document for more information.
    """
    json_path = os.environ.get('META_JSON_FILE_PATH', '')
    if not json_path:
        assert True
    else:
        with open(f"{json_path}/sample.json", "r",
                  encoding="utf-8") as j:
            raw = j.read()
        json_data = json.loads(raw)

        t1 = default_timer()
        meta = MetaJson(json_data)
        t2 = default_timer()

        print(f"\nLapse : {t2 - t1} seconds.\n")

        with open(f"{json_path}/sample_types.json", "w",
                  encoding="utf-8") as j:
            j.write(f"// Lapse : {t2 - t1} seconds.\n")
            j.write(str(meta.types))

        with open(f"{json_path}/sample_attrs.json", "w",
                  encoding="utf-8") as j:
            j.write(f"// Lapse : {t2 - t1} seconds.\n")
            j.write(str(meta.attributes))

        with open(f"{json_path}/sample_layers.json", "w",
                  encoding="utf-8") as j:
            j.write(f"// Lapse : {t2 - t1} seconds.\n")
            j.write(str(meta.layers))

        assert True
