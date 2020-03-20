import grovepi
import time
import sys


class WaterManager:

    relay_pin = 0

    def __init__(self):
        self.relay_pin = 3
        self.moisture_level_for_watering = 300
        self.water_level_for_watering = 200
        self.thread_give_water = None

        grovepi.pinMode(self.relay_pin, "OUTPUT")
        print('WATERMANAGER is ready.')

    def give_water(self, communication):
        communication.upload_watering()

        print('start pump')
        try:
            grovepi.digitalWrite(self.relay_pin, 1)
        except KeyboardInterrupt:
            grovepi.digitalWrite(self.relay_pin, 0)
            print('keyboardInterrupt: WaterManager, relay pin OFF')
        except IOError:
            print('IOError: WaterManager, relay pin ON')
        except:
            print('except: WaterManager, relay pin ON')
            print(sys.exc_info()[0])

        time.sleep(5)

        print('stop pump')
        try:
            grovepi.digitalWrite(self.relay_pin, 0)
        except KeyboardInterrupt:
            grovepi.digitalWrite(self.relay_pin, 0)
            print('keyboardInterrupt: WaterManager, relay pin OFF')
        except IOError:
            print('IOError: WaterManager, relay pin OFF')
        except:
            print('except: WaterManager, relay pin OFF')
            print(sys.exc_info()[0])

    def check_for_watering(self, measurement, communication):
        print('check_for_watering()')
        moisture = measurement.get_moisture()
        water_in_pot = measurement.get_water()

        if moisture < self.moisture_level_for_watering and water_in_pot > self.water_level_for_watering:
            self.give_water(communication)

    def run_test(self, measurement):
        print('run test for the watermanager')
        print('level moisture:', self.moisture_level_for_watering)
        print('current moisture:', measurement.get_moisture())
        print()
        print('level water:', self.water_level_for_watering)
        print('current water:', measurement.get_water())
        print()
        print('run pump for 5 seconds')
        grovepi.digitalWrite(self.relay_pin, 1)
        time.sleep(5)
        grovepi.digitalWrite(self.relay_pin, 0)
        print('finish pump after 5 seconds')

