import os
import requests


def get_location(address, city, state, zipcode):
    GEOCODE_API_KEY = os.environ.get('GEOCODE_API_KEY')

    base_url = "https://maps.googleapis.com/maps/api/geocode/json?address"

    formatted_address = address.replace(" ", "+")
    formatted_city = city.replace(" ", "+")

    endpoint = f"{base_url}={formatted_address},+{formatted_city},+{state}+{zipcode}&key={GEOCODE_API_KEY}"

    response = requests.get(endpoint).json()

    latitude = response["results"][0]["geometry"]["location"]["lat"]
    longitude = response["results"][0]["geometry"]["location"]["lng"]

    return latitude, longitude
