import requests
import db_connector
import sys

# Stałe
API_URL = "http://web:5000/users/"


def test_add_user(user_id, user_name):
    payload = {"user_name": user_name}
    response = requests.post(API_URL + str(user_id), json=payload)
    if response.status_code not in [200, 201] or response.json().get("user_added") != user_name:
        raise Exception(f"Test failed during ADD: {response.json()}")



def test_update_user(user_id, user_name):
    payload = {"user_name": user_name}
    response = requests.put(API_URL + str(user_id), json=payload)
    if response.status_code != 200 or response.json().get("user_updated") != user_name:
        raise Exception(f"Test failed during UPDATE: {response.json()}")


def test_get_user(user_id):
    response = requests.get(API_URL + str(user_id))
    if response.status_code != 200:
        raise Exception(
            f"Test failed: Error during GET request. Status Code: {response.status_code}, Response: {response.json()}")

    user_data = response.json()
    user_name = user_data.get("user_name")
    if not user_name:
        raise Exception("Test failed: No user_name returned in GET request")

    print(f"Data retrieved for user_id: {user_id}")
    print(f"User Name: {user_name}")

def verify_database_data(user_id, user_name):
    db_user_name = db_connector.get_user(user_id)
    if db_user_name != user_name:
        raise Exception("Test failed: Data mismatch in database")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: backend_testing.py <function_name> <user_id> [user_name]")
        sys.exit(1)

    function_name = sys.argv[1]
    user_id = int(sys.argv[2])
    user_name = sys.argv[3] if len(sys.argv) > 3 else None

    if function_name == "add":
        test_add_user(user_id, user_name)
        verify_database_data(user_id, user_name)
        print("User added successfully!")
    elif function_name == "update":
        test_update_user(user_id, user_name)
        verify_database_data(user_id, user_name)
        print("User updated successfully!")
    elif function_name == "get":
        test_get_user(user_id)
        print(f"Data retrieved for user_id: {user_id}")
    else:
        print(f"Unknown function name: {function_name}")
