import argparse
import db_connector
from selenium import webdriver

# Stałe
# WEB_INTERFACE_URL = "http://127.0.0.1:5001/users/get_user_data/"

if db_connector.is_running_in_docker:
    WEB_INTERFACE_URL = f"http://{db_connector.CURRENT_CONFIG['host']}:{db_connector.CURRENT_CONFIG['port']}/users/"
else:
    WEB_INTERFACE_URL = "http://127.0.0.1:5001/users/get_user_data/"


def test_frontend(user_id, element_id):
    # Uruchomienie przeglądarki
    driver = webdriver.Chrome()

    try:
        # Nawigacja do interfejsu webowego
        driver.get(WEB_INTERFACE_URL + str(user_id))

        # Sprawdzenie, czy element istnieje na stronie
        user_name_element = driver.find_element_by_id(element_id)

        # Wydrukowanie nazwy użytkownika
        print(f"User name for user_id {user_id}: {user_name_element.text}")
    finally:
        # Zamknięcie przeglądarki
        driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Frontend Testing for Web App")
    parser.add_argument("action", choices=["test"], help="Action to be performed. For now, only 'test' is supported.")
    parser.add_argument("user_id", type=int, help="User ID to be tested")
    parser.add_argument("--element_id", default="user", help="HTML element ID for the user name on the web page")

    args = parser.parse_args()

    if args.action == "test":
        test_frontend(args.user_id, args.element_id)