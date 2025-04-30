import requests
#import datetime

print("\nRequests library example:")

try:
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    if response.status_code == 200:
        data = response.json()
        print(f"API Response: {data}")

    else:
        print(f"Request failed with status code: {response.status_code}")
except Exception as e:
    print(f"Error making request: {e}")

