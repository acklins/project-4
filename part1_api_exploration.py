import requests

BASE_URLS = {
    "jsonplaceholder": "https://jsonplaceholder.typicode.com",
    "open-meteo": "https://api.open-meteo.com/v1/forecast",
}

#Print common HTTP response information.

def print_response_info(response):

    print("Method:", response.request.method)
    print("URI:", response.url)
    print(
        "Status:",
        response.status_code,
        response.reason
    )
    print(
        "Content-Type:",
        response.headers.get(
            "Content-Type",
            "Not specified"
        )
    )
#=================================
#API 1: JSONPlaceholder
#=================================

def explore_jsonplaceholder():

    print("\n=== API 1: JSONPlaceholder ===")

#REST concept: /users represents a collection resource.
print("\n--- 1. GET ALL USERS ---")

try:
    response = requests.get(
        f"{BASE_URLS['jsonplaceholder']}/users",
        timeout=10
    )

    print_response_info(response)
    response.raise_for_status()

    users = response.json()

    print("Number of users:", len(users))

    for user in users:
        print(
            f"{user['name']} - {user['email']}"
        )
except requests.RequestException as error:
    print("Request failed:", error)

#REST concept: /users/1 identifies one specific resource.
print("\n--- 2. GET USER 1 ---")

try:
    response = requests.get(
        f"{BASE_URLS['jsonplaceholder']}/users/1",
        timeout=10
    )

    print_response_info(response)
    response.raise_for_status()

    user = response.json()

    print("Name:", user["name"])
    print("Email:", user["email"])
    print("City:", user["address"]["city"])

except requests.RequestException as error:
    print("Request failed:", error)

#REST concept: Query parameters filter a collection.
print("\n--- 3. GET POSTS BY USER 3 ---")

params = {
    "userId": 3
}

try:
    response = requests.get(
        f"{BASE_URLS['jsonplaceholder']}/posts",
        params=params,
        timeout=10
    )

    print_response_info(response)
    response.raise_for_status()

    posts = response.json()

    print("Number of posts:", len(posts))

    if posts:
        print(
            "first post title:",
            posts[0]["title"]
        )
except requests.RequestException as error:
    print("Request failed:", error)

#REST concept: /users/1/posts is a nested resource.

print("\n--- 4. GET USER 1'S POSTS ---")

try:
    response = requests.get(
        f"{BASE_URLS['jsonplaceholder']}/users/1/posts",
        timeout=10
    )

    print_response_info(response)
    response.raise_for_status()

    posts = response.json()

    print("Number of posts:", len(posts))

    if posts:
        print(
            "First post:",
            posts[0]["title"]
        )
except requests.RequestException as error:
    print("Request failed:", error)

#REST concept: POST creates a resource.

print("\n--- 5. CREATE NEW POST ---")

new_post = {
    "title": "My Module 4 API Project",
    "body": "Learning how to consume REST APIs with Python.",
    "userId": 1
}

try: 
    response = requests.post(
        f"{BASE_URLS['jsonplaceholder']}/posts",
        json=new_post,
        timeout=10
    )

    print_response_info(response)
    response.raise_for_status()

    created_post = response.json()

    print(
        "Returned ID:",
        created_post["id"]
    )

    print(
        "Title:",
        created_post["title"]
    )
except requests.RequestException as error:
    print("Request failed:", error)

#==================================
# API 2: Open-Meteo
# ===================================

def explore_openmeteo():
    print("\n=== API 2: OPEN-METEO ===")

    params = {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "current": (
            "temperature_2m,"
            "apparent_temperature,"
            "relative_humidity_2m,"
            "wind_speed_10m"
        ),
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "timezone": "America/New_York"
    }

try:
    response = requests.get(
        BASE_URLS["open-meteo"],
        params=params,
        timeout=10
    )

    print_response_info(response)
    response.raise_for_status()

    weather = response.json()
    current = weather["current"]

    print("Location: New York City")
    print(
        "Temperature:",
        current["temperature_2m"],
        "F"
    )
    print(
        "Feels Like:",
        current["apparent_temperature"],
        "F"
    )
    print(
        "Humidity:",
        current["relative_humidity_2m"],
        "%"
    )
    print(
        "Wind Speed:",
        current["wind_speed_10m"],
        "mph"
    )
except requests.RequestException as error:
    print("Request failed:", error)
# =============================================
# RUN ALL EXPLORATIONS
# =============================================

if __name__ == "__main__":
    explore_jsonplaceholder()
    explore_openmeteo()

    print("\n=== Exploration complete! ===")
