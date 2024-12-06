Flight Tracker Application

This is a simple Flask web application that allows users to track the status of a flight by providing a flight number. The app fetches flight data from the AviationStack API and displays key flight details, including departure and arrival cities, flight status, and coordinates of the airports. The application also uses the OpenCage API to get the latitude and longitude of the departure and arrival cities.

Features

Flight tracking by IATA flight number.

Displays flight status (e.g., scheduled, delayed, landed).

Retrieves the departure and arrival cities along with their coordinates.

Simple, easy-to-use interface.


Prerequisites

Before running the app, make sure you have the following:

Python 3.x

Flask

Requests library

API keys for:

AviationStack for flight data.

OpenCage for geocoding city coordinates.



Setup

1. Clone the repository:

To clone this repository, run the following command in your terminal:

git clone https://github.com/EliezerSunny/flight-tracker.git

Replace your-username with your GitHub username.

2. Install required dependencies:

Navigate into the project directory:

cd flight-tracker

Install the required dependencies using pip:

pip install flask requests

3. Set up API keys:

Replace your_api_key with your actual API key from AviationStack in the code.

Replace your_api_key with your actual API key from OpenCage in the code.


API_KEY = "your_api_key"  # Replace with your actual AviationStack API key
OPENCAGE_API_KEY = "your_api_key"  # Replace with your OpenCage API key

4. Run the Flask application:

python app.py

The app will run locally at http://127.0.0.1:5000/.

5. Use the application:

Open your browser and visit the app's homepage.

Enter a flight number in the provided input field and submit the form to fetch the flight status and airport coordinates.


Application Workflow:

1. The user visits the homepage and enters a flight number.


2. The application sends a request to the AviationStack API to fetch flight data.


3. If the flight data is found, the app retrieves departure and arrival cities, their coordinates using the OpenCage API, and the flight's status.


4. The flight information is then displayed on the webpage.



Example Flight Data Display:

Flight number

Departure city with coordinates

Arrival city with coordinates

Flight status


Error Handling:

If the API request fails or no data is found, the user is informed with an error message.

In case of any exceptions, a generic error message is shown.


License

This project is open source and available under the MIT License. See the LICENSE file for details.

