import requests
import json

def test_response_data_types():
    # Send a GET request
    response = requests.get('https://reqres.in/api/users?page=2')

    # Parse the JSON response
    data = json.loads(response.text)

    # Now you can create assertions based on the data types you expect
    assert isinstance(data, dict), "Response is not a dictionary"
    assert isinstance(data.get('page'), int), "Page is not an integer"
    assert isinstance(data.get('per_page'), int), "Per_page is not an integer"
    assert isinstance(data.get('total'), int), "Total is not an integer"
    assert isinstance(data.get('total_pages'), int), "Total_pages is not an integer"
    assert isinstance(data.get('data'), list), "Data is not a list"

    # For each user in the data, check the expected data types
    for user in data.get('data', []):
        assert isinstance(user.get('id'), int), "User ID is not an integer"
        assert isinstance(user.get('email'), str), "User email is not a string"
        assert isinstance(user.get('first_name'), str), "User first name is not a string"
        assert isinstance(user.get('last_name'), str), "User last name is not a string"
        assert isinstance(user.get('avatar'), str), "User avatar is not a string"

    print("All assertions passed!")

if __name__ == "__main__":
    test_response_data_types()
