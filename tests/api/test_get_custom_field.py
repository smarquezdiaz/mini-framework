from pages.CustomFieldAPI import CustomFieldAPI
from pages.ResponseValidator import ResponseValidator

api = CustomFieldAPI()
validator = ResponseValidator()

field_ids = [1, 2, 3]

def generate_test(field_id):
    def test_func():
        response = api.get_custom_field(field_id)
        validator.validate_status_code(response, 200)
        json_resp = validator.validate_status_true(response)
        assert str(json_resp.get("result", {}).get("id")) == str(field_id)
    return test_func

for field_id in field_ids:
    test_name = f"test_get_custom_field_id_{field_id}"
    globals()[test_name] = generate_test(field_id)
