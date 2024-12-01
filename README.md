
Flight Tracker Application

A Flask-based web application to track flight details, including status, departure, arrival information, and a map visualization of the route.


---

Features

Search flights using their flight number.

Displays flight details such as departure, arrival cities, estimated times, and status (e.g., active, landed).

Visualizes flight routes on an interactive map using Leaflet.js.



---

Prerequisites

Before running this project, ensure you have the following:

1. Python 3.7+


2. Flask - A lightweight web framework.


3. API Keys:

AviationStack API: For flight data (sign up here).

OpenCage API: For geocoding airport locations (sign up here).



4. Basic understanding of running Python projects.




---

Project Setup

1. Clone the Repository

git clone https://github.com/eliezersunny/flight-tracker.git
cd flight-tracker

2. Install Dependencies

Create a virtual environment and install the required packages:

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

3. Configure API Keys

Create a .env file in the root directory to store your API keys:

API_KEY=your_aviationstack_api_key
OPENCAGE_API_KEY=your_opencage_api_key

4. Run the Application

Run the Flask application:

python app.py

The app will be accessible at http://127.0.0.1:5000/.


---

Project Structure

flight-tracker/
├── static/
│   └── style.css  # Custom CSS for styling
├── templates/
│   └── index.html # HTML template for the application
├── app.py          # Main Flask application
├── requirements.txt # Python dependencies
└── README.md       # Project documentation


---

How to Use

1. Navigate to the homepage at http://127.0.0.1:5000/.


2. Enter a flight number (e.g., AA123, AC103 ...) in the search bar.


3. Click "Search" to view:

Departure city and estimated time.

Arrival city and estimated time.


Flight status (e.g. scheduled, active, landed).

Interactive map showing the departure and arrival points.





---

APIs Used

1. AviationStack API

Provides flight information like status, departure, and arrival details.

Example endpoint:
http://api.aviationstack.com/v1/flights


2. OpenCage API

Converts city names into geographical coordinates for map visualization.

Example endpoint:
https://api.opencagedata.com/geocode/v1/json



---

Troubleshooting

Common Errors and Fixes

1. "API request failed":

Ensure your API keys are correctly configured in the .env file.

Check your internet connection.



2. "No flight data found":

Verify that the entered flight number is valid and currently active.



3. Map not loading:

Ensure Leaflet.js is properly linked in the index.html file.





---

Future Improvements

Add user authentication for personalized tracking.

Cache flight data to reduce API requests.

Add support for multi-language.



---

License

This project is licensed under the MIT License.


---

Acknowledgements

AviationStack API for flight data.

OpenCage API for geocoding.

Leaflet.js for interactive maps.



---

Author

Developed by EliezerSunny. Feel free to reach out for suggestions or contributions!





Airline Codes and Numbers List

This document provides a reference for airline codes, also known as airline designators, assigned by the International Air Transport Association (IATA) or the International Civil Aviation Organization (ICAO). These codes are essential for identifying airlines and their flights.

IATA Airline Codes

AA - American Airlines

AC - Air Canada

AF - Air France

BA - British Airways

CA - Air China

DL - Delta Air Lines

EK - Emirates

LH - Lufthansa

QF - Qantas

UA - United Airlines


ICAO Airline Codes

AAL - American Airlines

ACA - Air Canada

AFR - Air France

BAW - British Airways

CCA - Air China

DAL - Delta Air Lines

UAE - Emirates

DLH - Lufthansa

QFA - Qantas

UAL - United Airlines


Airline Call Signs (Telephony Designators)

American Airlines - "American"

Air Canada - "Maple"

Air France - "Airfrans"

British Airways - "Speedbird"

Air China - "China Air"

Delta Air Lines - "Delta"

Emirates - "Emirates"

Lufthansa - "Lufthansa"

Qantas - "Qantas"

United Airlines - "United"


Airline Codes for Airlines Beginning with Specific Letters

TE: Used by TEAL from 1940–1965, then Air New Zealand from 1965–1990

LM: Gained by Air New Zealand after beginning independent operations in 2017


> Note:
The list of airline codes and numbers is not exhaustive and is subject to change.


