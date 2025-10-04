class ResponseValidator:

    def validate_status_code(self, response, expected_code=200):
        assert response.status_code == expected_code, \
            f" Expected {expected_code}, got {response.status_code}"

    def validate_status_true(self, response):
        json_resp = response.json()
        assert json_resp["status"] is True, " API status is not True"
        return json_resp
