# Flight Tracker Application

This is a simple Flask web application that allows users to track the status of a flight by providing a flight number. The app fetches flight data from the AviationStack API and displays key flight details, including departure and arrival cities, flight status, and coordinates of the airports. The application also uses the OpenCage API to get the latitude and longitude of the departure and arrival cities.


---

## Features

Flight tracking by IATA flight number.

Displays flight status (e.g., scheduled, delayed, landed).

Retrieves departure and arrival cities along with their coordinates.

Simple, easy-to-use interface.



---

## Prerequisites

Before running the app, make sure you have the following:

Python 3.x

Flask and Requests libraries

API keys for:

AviationStack for flight data.

OpenCage for geocoding city coordinates.




---

## Setup

1. Clone the Repository

Clone this repository to your local machine by running the following command in your terminal:

git clone https://github.com/EliezerSunny/flight-tracker.git

Replace your-username with your actual GitHub username.

2. Install Required Dependencies

Navigate to the project directory:

cd flight-tracker

Install the required dependencies using pip:

pip install flask requests

3. Set Up API Keys

Replace the placeholder API keys in the code with your actual keys:

API_KEY = "your_api_key"  # Replace with your actual AviationStack API key
OPENCAGE_API_KEY = "your_api_key"  # Replace with your OpenCage API key

4. Run the Flask Application

To start the application, run the following command:

python app.py

The app will be hosted locally at http://127.0.0.1:5000/.


---

## Usage

1. Open your browser and visit the application’s homepage (http://127.0.0.1:5000/).


2. Enter a flight number in the provided input field and submit the form.


3. The application will fetch flight details, including:

Flight status

Departure and arrival cities with their coordinates



4. The flight information will be displayed on the webpage.




---

## Application Workflow

1. The user visits the homepage and enters a flight number.


2. The application sends a request to the AviationStack API to fetch flight data.


3. If the flight data is found:

The app retrieves departure and arrival cities.

It uses the OpenCage API to get the coordinates of the cities.

Displays flight status and coordinates for both airports.



4. The flight information is then rendered on the webpage.




---

## Example Flight Data Display

Flight number

Departure city with coordinates

Arrival city with coordinates

Flight status



---

## Error Handling

If the API request fails or no data is found, an error message is displayed.

If any exception occurs during data retrieval, a generic error message will be shown to the user.



---

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.
