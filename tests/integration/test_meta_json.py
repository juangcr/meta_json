import pytest
import json
from pathlib import Path
from datetime import datetime
from meta_json.meta_json import MetaJson

def test_integration():
    
    with open(f"{Path(__file__).resolve().parents[0]}/sample.json", "r",
              encoding="utf-8") as j:
        raw = j.read()
    json_data = json.loads(raw)

    t1 = datetime.now()
    meta = MetaJson(json_data)
    t2 = datetime.now()

    with open(f"{Path(__file__).resolve().parents[0]}/sample_types.json", "w",
              encoding="utf-8") as j:
        j.write(f"// Lapse : {t2 - t1} sec\n")
        j.write(str(meta.types))

    with open(f"{Path(__file__).resolve().parents[0]}/sample_attrs.json", "w",
              encoding="utf-8") as j:
        j.write(f"// Lapse : {t2 - t1} sec\n")
        j.write(str(meta.attributes))

    with open(f"{Path(__file__).resolve().parents[0]}/sample_layers.json", "w",
              encoding="utf-8") as j:
        j.write(f"// Lapse : {t2 - t1} sec\n")
        j.write(str(meta.layers))

    assert True
