import time

import pflanzen.output as output
import pflanzen.measure as measure
import pflanzen.communication as communication
import pflanzen.watering as watering
import pflanzen.config as config

def test():
    print()
    print('------------------ TESTS --------------------')
    print()
    outputManager.run_test()
    measurementManager.run_test()
    communicationManager.run_test()
    waterManager.run_test(measurementManager)
    print()
    print('---------------------------------------------')
    print()


def set_values():
    waterManager.set_pump_duration(pump_duration)
    waterManager.set_water_level_for_watering(water_level_dry)
    waterManager.set_moisture_level_for_watering(moisture_level_dry)


def run():
    measurementManager.start_measurements()

    while True:
        # Do the following repeatedly:
        measurementManager.do_measurements()
        outputManager.show_moisture_on_led_bar(measurementManager)
        communicationManager.upload_measures(measurementManager)
        if config.water_stop < 1:
            config.gave_water = waterManager.check_for_watering(measurementManager, communicationManager)
        else:
            config.water_stop = config.water_stop - 1

        if config.gave_water:
            config.water_stop = config.water_stop_duration

        # Repeat all 'duration' seconds:
        time.sleep(duration)


# ----------------
# Define variables
# ----------------
# fix values
short_duration = 30
long_duration = 900
pump_duration = 4
moisture_level_dry = 240
water_level_dry = 200

# changing values
duration = long_duration

# classes
outputManager = output.OutputManager()
measurementManager = measure.MeasurementManager()
communicationManager = communication.CommunicationManager()
waterManager = watering.WaterManager()

# ---------------
# Run the program
# ---------------
set_values()
test()
run()
