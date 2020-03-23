import requests
import simplejson


class CommunicationManager:

    def __init__(self):
        # Init CommunicationManager
        # Set plant-id and all URLs
        self.url_measure = 'https://temperli.io/web/api/v1/measure'
        self.url_watering = 'https://temperli.io/web/api/v1/watering'
        self.token = 'aJHxrTWKJT14XZoHpHRUQLZVKrRYDDpe'
        self.plant_id = 5

        print('COMMUNICATIONMANAGER is ready.')

    def upload_measures(self, measurement):
        # Upload measurements to the browser

        print('upload_measures()')

        params = {
            'token': self.token,
            'plant_id': self.plant_id,
            'temperature': measurement.get_temperature(),
            'humidity_air': measurement.get_humidity(),
            'water_pot': measurement.get_water(),
            'moisture_earth': measurement.get_moisture(),
        }

        print('post', self.url_measure)

        # sending post request and saving the response as response object
        r = requests.post(url=self.url_measure, params=params)

        # extracting data in json format
        try:
            data = r.json()
            print(data)
        except simplejson.errors.JSONDecodeError:
            print('JSONDecodeError')
            print(r)

    def upload_watering(self):
        # Upload a current watering to the server

        params = {
            'token': self.token,
            'plant_id': self.plant_id,
            'watering': True
        }

        print('post', self.url_watering)

        # sending post request and saving the response as response object
        r = requests.post(url=self.url_watering, params=params)

        # extracting data in json format
        try:
            data = r.json()
            print(data)
        except simplejson.errors.JSONDecodeError:
            print('JSONDecodeError')
            print(r)

    def run_test(self):
        # Run tests for the CommunicationManager
        print('todo: test the communication to', self.url_measure)
