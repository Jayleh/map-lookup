import os
import datetime as dt
import requests
import pandas as pd
import datedelta


def get_location_from_search(address):
    GEOCODE_API_KEY = os.environ.get('GEOCODE_API_KEY')

    base_url = "https://maps.googleapis.com/maps/api/geocode/json?address"

    endpoint = f"{base_url}={address}&key={GEOCODE_API_KEY}"

    response = requests.get(endpoint).json()

    # print(response)

    try:
        latitude = response["results"][0]["geometry"]["location"]["lat"]
        longitude = response["results"][0]["geometry"]["location"]["lng"]

        details = {
            "formatted_address": response["results"][0]["formatted_address"],
            "latlng": [latitude, longitude]
        }

        return details

    except Exception as e:
        print(e)
        raise


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


class ImportHandler(object):

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


def get_time_now():
    time_now = dt.datetime.today() - dt.timedelta(hours=7)
    time_now = time_now.strftime("%Y%m%d%I%M%S")

    return time_now


class ExportHandler(object):

    def __init__(self, dir_name):
        self.dir_name = dir_name

    def empty_folder(self):
        # Delete any files in uploads folder
        files = os.listdir(self.dir_name)

        for file in files:
            os.remove(os.path.join(self.dir_name, file))

    def check_export(self):
        files = os.listdir(self.dir_name)

        for file in files:
            if file != ".gitignore":
                return file

        return None

    def handle_export(self, db):
        data = []

        for reseller in db:
            reseller_data = {
                "id": reseller.id,
                "first_name": reseller.first_name,
                "last_name": reseller.last_name,
                "phone": reseller.phone,
                "email": reseller.email,
                "company": reseller.company,
                "address": reseller.address,
                "city": reseller.city,
                "state": reseller.state,
                "zipcode": reseller.zipcode,
                "latitude": reseller.latitude,
                "longitude": reseller.longitude,
                "comments": reseller.comments,
                "action": ""
            }
            data.append(reseller_data)

        df = pd.DataFrame(data)

        columns = ["id", "first_name", "last_name", "phone", "email", "company", "address",
                   "city", "state", "zipcode", "latitude", "longitude", "comments", "action"]

        df = df[columns]

        time = get_time_now()

        df.to_csv(f"{self.dir_name}{time}_resellers_export.csv", encoding="utf-8", index=False)
