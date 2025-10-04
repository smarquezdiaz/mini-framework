from jsonschema import validate

def test_get_attachments_schema(api_session, attachments_schema):
    url = "https://api.qase.io/v1/attachment?limit=10&offset=0"
    response = api_session.get(url)

    # Validar código de estado
    assert response.status_code == 200, f"Status inesperado: {response.status_code}"

    # Validar estructura JSON
    data = response.json()
    validate(instance=data, schema=attachments_schema)
