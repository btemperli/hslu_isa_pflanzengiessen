import grovepi
import time


class WaterManager:

    relay_pin = 0
    pump_duration = 0
    water_level_for_watering = 0
    moisture_level_for_watering = 0

    def __init__(self):
        # Init Water Manager
        # - set relay_pin
        # - set watering levels
        self.relay_pin = 3

        grovepi.pinMode(self.relay_pin, "OUTPUT")
        print('WATERMANAGER is ready.')

    def set_pump_duration(self, pump_duration):
        self.pump_duration = pump_duration

    def set_water_level_for_watering(self, water_level):
        self.water_level_for_watering = water_level

    def set_moisture_level_for_watering(self, moisture_level):
        self.moisture_level_for_watering = moisture_level

    def give_water(self, communication):
        # Give Water
        # - Upload the message to the server
        # - start pump
        # - wait x seconds (pump is running)
        # - stop pump
        communication.upload_watering()

        print('start pump')
        try:
            grovepi.digitalWrite(self.relay_pin, 1)
        except KeyboardInterrupt:
            grovepi.digitalWrite(self.relay_pin, 0)
            print('keyboardInterrupt: WaterManager, relay pin OFF')
        except IOError:
            print('IOError: WaterManager, relay pin ON')

        time.sleep(self.pump_duration)

        print('stop pump')
        try:
            grovepi.digitalWrite(self.relay_pin, 0)
        except KeyboardInterrupt:
            grovepi.digitalWrite(self.relay_pin, 0)
            print('keyboardInterrupt: WaterManager, relay pin OFF')
        except IOError:
            print('IOError: WaterManager, relay pin OFF')

    def check_for_watering(self, measurement, communication):
        # Check for Watering, look if water is needed by the plant:
        # - get moisture value
        # - get water value
        # - give water if values are in range

        print('check_for_watering()')
        moisture = measurement.get_moisture()
        water_in_pot = measurement.get_water()

        if moisture < self.moisture_level_for_watering and water_in_pot > self.water_level_for_watering:
            self.give_water(communication)
            return True

        return False

    def run_test(self, measurement):
        # Run Tests in the WaterManager

        print('run test for the watermanager')
        print('level moisture:', self.moisture_level_for_watering)
        print('current moisture:', measurement.get_moisture())
        print()
        print('level water:', self.water_level_for_watering)
        print('current water:', measurement.get_water())
        print()
        print('run pump for 0.1 seconds')
        grovepi.digitalWrite(self.relay_pin, 1)
        time.sleep(0.1)
        grovepi.digitalWrite(self.relay_pin, 0)
        print('finish pump after 0.1 seconds')

