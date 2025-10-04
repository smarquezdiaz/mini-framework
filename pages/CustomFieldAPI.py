from utils.api_client import post, get

class CustomFieldAPI:

    def create_custom_field(self, title: str, entity: int, type_: int):
        payload = {
            "title": title,
            "entity": entity,
            "type": type_
        }
        return post("/custom_field", payload)

    def get_custom_field(self, field_id: int):
        return get(f"/custom_field/{field_id}")
