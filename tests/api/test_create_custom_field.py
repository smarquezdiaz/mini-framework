import os
import json
from pages.CustomFieldAPI import CustomFieldAPI
from pages.ResponseValidator import ResponseValidator

def test_create_custom_fields():
    api = CustomFieldAPI()
    validator = ResponseValidator()

    data_path = os.path.join(
        os.path.dirname(__file__), "..", "..", "data", "custom_fields.json"
    )

    with open(data_path, encoding="utf-8") as f:
        custom_fields = json.load(f)

    for field in custom_fields:
        response = api.create_custom_field(field["title"], field["entity"], field["type"])

        validator.validate_status_code(response, 200)
        json_resp = validator.validate_status_true(response)
        assert "result" in json_resp
