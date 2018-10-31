import os
import requests
import pandas as pd


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


def get_dataframe(dir_name, file):
    full_path = f"{dir_name}{file}"

    file_extension = os.path.splitext(full_path)[1]

    if file_extension == ".xls" or file_extension == ".xlsx":
        return pd.read_excel(full_path, encoding="utf-8")
    elif file_extension == ".csv":
        return pd.read_csv(full_path, encoding="utf-8")

    return None


class FileHandler(object):

    def __init__(self, dir_name):
        self.dir_name = dir_name

    def empty_folder(self):
        # Delete any files in uploads folder
        files = os.listdir(self.dir_name)

        for file in files:
            os.remove(os.path.join(self.dir_name, file))

    def handle_import_file(self):
        file = os.listdir(self.dir_name)[0]

        df = get_dataframe(self.dir_name, file)

        return df
