import unittest
import requests
import json
import time
from jsonschema import validate, ValidationError

class TestPOST(unittest.TestCase):
    def setUp(self):
        self.url = "https://reqres.in/api/users"
        self.headers = {'Content-Type': 'application/json'}
        self.data_file_path = 'data.json'  # Path to your data file
        self.response_time_limit = 100  # in milliseconds
        self.schema = {  # Define your schema here
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "createdAt": {"type": "string"}
            },
            "required": ["id", "createdAt"]
        }

    def load_data(self):
        with open(self.data_file_path, 'r') as file:
            data = json.load(file)
        return data

    def test_create(self):
        data = self.load_data()
        start_time = time.time()
        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))
        end_time = time.time()

        # Assert HTTP status code
        self.assertEqual(response.status_code, 201)

        # Assert ID and timestamp of createdAt
        response_data = response.json()
        self.assertIn('id', response_data)
        self.assertIn('createdAt', response_data)

        # Assert response schema
        try:
            validate(instance=response_data, schema=self.schema)
        except ValidationError as e:
            self.fail(f"Response schema validation failed: {e.message}")

        # Assert response time
        response_time = (end_time - start_time) * 1000  # Convert to milliseconds
        self.assertLess(response_time, self.response_time_limit)

if __name__ == "__main__":
    unittest.main()
