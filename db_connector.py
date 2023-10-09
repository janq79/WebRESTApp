import pymysql
import datetime
from pymysql.cursors import DictCursor

# W prawdziwej aplikacji warto przenieść te dane do pliku konfiguracyjnego lub zmiennych środowiskowych.
CONFIG = {
    'host': 'db',
    'port': 3306,
    'user': 'user',
    'password': 'password',
    'db': 'mydb'
}

# Prosta pula połączeń
class ConnectionPool:
    def __init__(self):
        self.connection = pymysql.connect(**CONFIG, cursorclass=DictCursor, autocommit=True)

    def get_connection(self):
        return self.connection

pool = ConnectionPool()

def connect_to_db():
    return pool.get_connection()

def get_next_available_id():
    try:
        with connect_to_db().cursor() as cursor:
            cursor.execute("SELECT MAX(user_id) FROM users")
            result = cursor.fetchone()
            return (result["user_id"] if result["user_id"] else 0) + 1
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def add_user(user_id, user_name):
    try:
        creation_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with connect_to_db().cursor() as cursor:
            cursor.execute("INSERT INTO users (user_id, user_name, creation_date) VALUES (%s, %s, %s)", (user_id, user_name, creation_date))
        return user_id
    except pymysql.err.IntegrityError:
        new_user_id = get_next_available_id()
        with connect_to_db().cursor() as cursor:
            cursor.execute("INSERT INTO users (user_id, user_name, creation_date) VALUES (%s, %s, %s)", (new_user_id, user_name, creation_date))
        return new_user_id
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def get_user(user_id):
    try:
        with connect_to_db().cursor() as cursor:
            cursor.execute("SELECT user_name FROM users WHERE user_id = %s", (user_id,))
            result = cursor.fetchone()
            return result["user_name"] if result else None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def update_user(user_id, user_name):
    try:
        with connect_to_db().cursor() as cursor:
            cursor.execute("UPDATE users SET user_name = %s WHERE user_id = %s", (user_name, user_id))
    except Exception as e:
        print(f"Error occurred: {e}")

def delete_user(user_id):
    try:
        with connect_to_db().cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
    except Exception as e:
        print(f"Error occurred: {e}")

def get_config_data():
    try:
        with connect_to_db().cursor() as cursor:
            cursor.execute("SELECT api_gateway_url, browser_type, user_name_to_insert FROM config LIMIT 1")
            result = cursor.fetchone()
            if result:
                return result
            else:
                raise Exception("No configuration data found in the database.")
    except Exception as e:
        print(f"Error occurred: {e}")
        return None