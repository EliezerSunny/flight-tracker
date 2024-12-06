Flight Tracker API

Overview

The Flight Tracker API allows users to retrieve real-time flight information, including flight numbers, airlines, and departure/arrival airports. This API integrates with third-party services like AviationStack to provide accurate and up-to-date flight data.

The application is designed to be lightweight, stateless, and easy to integrate into any web or mobile application that requires flight tracking.


---

Features

Retrieve live flight information (flight numbers, airlines, airports).

Filter flights by departure and arrival locations.

Support for multiple airlines and flight statuses.

Error handling for invalid requests or failed external API calls.

Simple, RESTful design for easy consumption.



---

Technologies Used

Flask - Web framework for building the API.

AviationStack API - Third-party service for real-time flight data.

Python - Programming language.

Flask-Caching - To cache flight data and improve performance.

Requests - To make HTTP requests to the AviationStack API.



---

Setup & Installation

Prerequisites

Before running the project, ensure you have the following:

Python 3.7+ installed.

A free API key from AviationStack.


Installation Steps

1. Clone the repository:

git clone https://github.com/EliezerSunny/flight-tracker.git
cd flight-tracker-api


2. Create a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. Install dependencies:

pip install -r requirements.txt


4. Set up your AviationStack API key:

Create a .env file in the root directory of the project.

Add your API key like this:

AVIATIONSTACK_API_KEY=your_api_key_here



5. Run the application:

python app.py

Your API will be available at http://localhost:5000.




---

API Endpoints

1. Get all flights

URL: /flights

Method: GET

Query Parameters:

departure: (Optional) Filter by departure airport code (e.g., JFK).

arrival: (Optional) Filter by arrival airport code (e.g., LAX).


Response:

[
  {
    "flight_number": "AA123",
    "airline": "American Airlines",
    "departure": "JFK",
    "arrival": "LAX",
    "status": "On Time"
  },
  {
    "flight_number": "DL456",
    "airline": "Delta Airlines",
    "departure": "ATL",
    "arrival": "ORD",
    "status": "Delayed"
  }
]


2. Get flight by number

URL: /flights/{flight_number}

Method: GET

URL Parameters:

flight_number: The flight number (e.g., AA123).


Response:

{
  "flight_number": "AA123",
  "airline": "American Airlines",
  "departure": "JFK",
  "arrival": "LAX",
  "status": "On Time"
}



---

Error Handling

The API returns standard HTTP status codes to indicate success or failure:

200 OK: Successfully processed the request.

400 Bad Request: Invalid or missing parameters.

404 Not Found: No flights found for the given criteria.

500 Internal Server Error: If there's an issue with the external API or server.



---

Testing the API

To test the API endpoints, you can use tools like Postman or cURL. For example, to get all flights:

curl http://localhost:5000/flights?departure=JFK&arrival=LAX


---

Future Improvements

Add authentication: Implement token-based authentication to protect sensitive endpoints.

Store flight data: Integrate a database to persist flight data and reduce dependency on external APIs.

Real-time updates: Implement a WebSocket-based solution for pushing real-time flight updates.

Advanced filters: Allow filtering by more criteria (e.g., flight status, airline).



---

License

This project is licensed under the MIT License - see the LICENSE file for details.


---

Contact

For any questions, feel free to reach out at @eliezersunny.

