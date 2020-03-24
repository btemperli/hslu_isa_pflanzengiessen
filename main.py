import threading
import time

import pflanzenprojekt.pflanzen.output as output
import pflanzenprojekt.pflanzen.measure as measure
import pflanzenprojekt.pflanzen.communication as communication
import pflanzenprojekt.pflanzen.watering as watering

duration = 300

outputManager = output.OutputManager()
measurement = measure.Measurement()
communicationManager = communication.CommunicationManager()
waterManager = watering.WaterManager()

print()
print('------------------ TESTS --------------------')
print()

outputManager.run_test()
measurement.run_test()
communicationManager.run_test()
waterManager.run_test(measurement)

print()
print('---------------------------------------------')
print()

measurement.start_measurements()

while True:
    # Do the following repeatedly:
    measurement.do_measurements()
    outputManager.show_moisture_on_led_bar(measurement)
    communicationManager.upload_measures(measurement)
    waterManager.check_for_watering(measurement, communicationManager)

    # Repeat all 'duration' seconds:
    time.sleep(duration)
