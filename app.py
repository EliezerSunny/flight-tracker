from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "your_api_key"  # Replace with your actual API key
BASE_URL = "http://api.aviationstack.com/v1/flights"
OPENCAGE_API_KEY = "your_api_key"  # Replace with your OpenCage API key

# Function to get latitude and longitude for airport locations using OpenCage API
def get_coordinates(city_name):
    geocode_url = f"https://api.opencagedata.com/geocode/v1/json?q={city_name}&key={OPENCAGE_API_KEY}"
    response = requests.get(geocode_url)
    data = response.json()
    if data['results']:
        lat = data['results'][0]['geometry']['lat']
        lon = data['results'][0]['geometry']['lng']
        return lat, lon
    return None, None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    flight_number = request.form['flight_number']  # Get the flight number from the form
    params = {
        'access_key': API_KEY,
        'flight_iata': flight_number  # Pass the flight number as a query parameter
    }

    try:
        # Make the API request to get flight data
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            return render_template('index.html', error="API request failed.")

        if not data.get('data'):
            return render_template('index.html', error="No flight data found.")

        flight_info = data['data'][0]
        departure_city = flight_info['departure']['airport']
        arrival_city = flight_info['arrival']['airport']
        flight_status = flight_info.get('flight_status', 'Unknown')  # Extract flight status

        # Get coordinates for both departure and arrival cities
        departure_lat, departure_lon = get_coordinates(departure_city)
        arrival_lat, arrival_lon = get_coordinates(arrival_city)

        # Add coordinates and status to flight_info
        flight_info['departure']['latitude'] = departure_lat
        flight_info['departure']['longitude'] = departure_lon
        flight_info['arrival']['latitude'] = arrival_lat
        flight_info['arrival']['longitude'] = arrival_lon
        flight_info['status'] = flight_status  # Add status to the flight info
        flight_info['flight_number'] = flight_number  # Add the flight number to the info

        return render_template('index.html', flight_info=flight_info)

    except Exception as e:
        return render_template('index.html', error=f"An error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)
