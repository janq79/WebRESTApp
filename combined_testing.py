import argparse
import requests
from selenium import webdriver

# Stałe
WEB_INTERFACE_URL = "http://127.0.0.1:5001/users/get_user_data/"
API_ENDPOINT = "http://127.0.0.1:5000/users/"


def test_backend(user_id):
    response = requests.get(API_ENDPOINT + str(user_id))
    data = response.json()

    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code} from backend.")
        return None

    return data.get("user_name")


def test_frontend(user_id, element_id):
    driver = webdriver.Chrome()

    try:
        driver.get(WEB_INTERFACE_URL + str(user_id))
        user_name_element = driver.find_element_by_id(element_id)
        return user_name_element.text
    finally:
        driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combined Testing for Web App")
    parser.add_argument("action", choices=["test"], help="Action to be performed. For now, only 'test' is supported.")
    parser.add_argument("user_id", type=int, help="User ID to be tested")
    parser.add_argument("--element_id", default="user", help="HTML element ID for the user name on the web page")

    args = parser.parse_args()

    if args.action == "test":
        backend_name = test_backend(args.user_id)
        frontend_name = test_frontend(args.user_id, args.element_id)

        if backend_name == frontend_name:
            print(f"Success! Backend and Frontend names match: {backend_name}")
        else:
            print(f"Error: Backend returned name '{backend_name}' while Frontend showed name '{frontend_name}'")