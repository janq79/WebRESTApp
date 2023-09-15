import requests

try:
    requests.get('http://127.0.0.1:5000/stop_server')
except Exception as e:
    print("Error stopping rest_app server:", e)

try:
    requests.get('http://127.0.0.1:5001/stop_server')
except Exception as e:
    print("Error stopping web_app server:", e)