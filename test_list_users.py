import requests
import json

# Send a GET request
response = requests.get('https://reqres.in/api/users')

# Check if the request was successful
if response.status_code == 200:
    # Parse the response
    data = json.loads(response.text)

    # Assert 'total'
    total = data['total']
    print(f"Total users: {total}")

    # Assert 'last_name' for the first and second user in 'data'
    first_user_last_name = data['data'][0]['last_name']
    second_user_last_name = data['data'][1]['last_name']
    print(f"First user's last name: {first_user_last_name}")
    print(f"Second user's last name: {second_user_last_name}")

    # Count number of received users in 'data'
    num_users = len(data['data'])
    print(f"Number of users received in 'data': {num_users}")

    # Compare it to the received value 'total'
    if num_users == total:
        print("The number of users in 'data' matches the 'total' value.")
    else:
        print("The number of users in 'data' does not match the 'total' value.")
else:
    print(f"Request failed with status code: {response.status_code}")