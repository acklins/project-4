Module 4 - API Documentation

API 1: JSON Placeholder

Base URL
https://jsonplaceholder.typicode.com

Authentication

None.

JSONPlaceholder is a public testing API and does not require an API key or authentication token for the endpoints tested in this project.

Endpoints Tested

Method  Path       Description           Example Response Shape
GET     /users     Returns the           Array of user objects
                   collection
                   of users
GET     /users/1   Returns user 1        Single user object

GET     /posts?    Filters posts         Array of
        userId=3   to user 3             post objects

GET  /users/1/posts Returns the         Array of post objects
                    posts belonging 
                    to user 1
POST    /posts      Simulates creating  Created post object 
                    a new post          with an ID

Example User Response
{
    "id": 1,
    "name": "Example Name",
    "email": "example@example.com",
    "address": {
        "city": "Example City"
    }
}
Example Post Response
{
    "userId": 1,
    "id": 101,
    "title": "My Module 4 API Project",
    "body": "Learning how to consume REST APIs with Python."
}
Rate Limits Observed
I did not encounter a rate-limit error during my testing. I inspected the response headers returned during the project and did not rely on a specific rate limit that I could not verify from my requests.

Something Unexpected

JSONPlaceholder accepts POST requests and returns a successful response, but it is a testing API and does not permanently save the newly created resource. This demonstrated that receiving a successful HTTP response does not necessarily mean a testing API permanently changed its database.

API 2: Open-Meteo

Base URL
https://api.open-meteo.com/v1/forecast

Authentication

None for the public forecast request used in this project.

Endpoint Tested

Method  Path            Description           Example Response Shape
GET     /v1/forecast    Retrieves weather     Object containing
                        information using     location information
                        latitude, longitude,  and a nested current
                        and requested         weather object
                        weather variables 

Query Parameters Used

The request included:

latitude
longitude
current
temperature_unit
wind_speed_unit
timezone

The latitude and longitude represented New York City.

Example Response Shape
{
    "latitude": 40.7,
    "longitude": -74.0,
    "current": {
        "temperature_2m": 70.0,
        "apparent_temperature": 69.0,
        "relative_humidity_2m": 60,
        "wind_speed_10m": 5.0
    }
}

The numerical values above illustrate the response structure. Actual weather values depend on conditions when the request is made.

Rate Limits Observed

I did not encounter a rate-limit error while making the requests used for this project.

Something Unexpected

Open-Meteo's documentation website is not the same URL as the API endpoint. The documentation is available at open-meteo.com/en/docs, while the forecast request is sent to the /v1/forecast API endpoint. The API also requires location information such as latitude and longitude rather than a city name for the forecast request used in this project.

