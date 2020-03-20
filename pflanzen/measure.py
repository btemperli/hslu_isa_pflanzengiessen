import grovepi
import time
import math
import sys


class Measurement:

    temperature_pin = 0
    moisture_pin = 0
    water_pin = 0

    temperature = 0
    humidity = 0
    moisture = 0
    water = 0

    sensors = ['temperature', 'humidity', 'moisture', 'water']

    def __init__(self):
        # Digital
        self.temperature_pin = 4

        # Analog
        self.moisture_pin = 0
        self.water_pin = 1

        grovepi.pinMode(self.temperature_pin, "INPUT")
        grovepi.pinMode(self.moisture_pin, "INPUT")
        grovepi.pinMode(self.water_pin, "INPUT")

        print('MEASUREMENT is ready.')

    def measure(self):
        print('measure()')

        temperature = None
        humidity = None
        water = None
        moisture = None

        try:
            [temperature, humidity] = grovepi.dht(self.temperature_pin, 1)
            water = grovepi.analogRead(self.water_pin)
            moisture = grovepi.analogRead(self.moisture_pin)
        except KeyboardInterrupt:
            print('keyboardinterrupt in Measurement: measure data')
        except IOError:
            print('IOError in Measurement: measure data')
        except:
            print('except in Measurement: measure data')
            print(sys.exc_info()[0])

        if math.isnan(temperature):
            print('temperature is not a number!')
            temperature = None
        if math.isnan(humidity):
            print('humidity is not a number!')
            humidity = None
        if math.isnan(water):
            print('water is not a number!')
            water = None
        if math.isnan(moisture):
            print('moisture is not a number!')
            moisture = None

        return {
            'temperature': temperature,
            'humidity': humidity,
            'water': water,
            'moisture': moisture
        }

    def get_moisture(self):
        return self.moisture

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_water(self):
        return self.water

    def print_measurements(self, measurements):
        for sensor in self.sensors:
            print(sensor + ':', measurements[sensor])
        print()

    def start_measurements(self):
        measurements = self.measure()
        self.print_measurements(measurements)

        for sensor in self.sensors:
            setattr(self, sensor, measurements[sensor])

    def do_measurements(self):
        measurements = self.measure()

        for sensor in self.sensors:
            if measurements[sensor] and getattr(self, sensor) != measurements[sensor] and not math.isnan(measurements[sensor]):
                setattr(self, sensor, measurements[sensor])
                print('new', sensor + ':', measurements[sensor])

    def run_test(self):
        print('run test for measurement:')

        try:
            for i in range(0, 4):
                measurements = self.measure()
                self.print_measurements(measurements)
                time.sleep(1)
        except IOError:
            print('MeasureError: Sensors are not working.')
        except:
            print('run_test measure.py: except error')
            print(sys.exc_info()[0])
