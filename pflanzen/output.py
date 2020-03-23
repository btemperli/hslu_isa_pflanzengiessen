import grovepi
import time
import math


class OutputManager:

    led_bar = 0

    def __init__(self):
        self.led_bar = 6

        grovepi.pinMode(self.led_bar, "OUTPUT")
        grovepi.ledBar_init(self.led_bar, 0)
        print('OUTPUTMANAGER is ready.')

    def show_moisture_on_led_bar(self, measurement):
        print('show_moisture_on_led_bar()')
        value = measurement.get_moisture()

        #       Min  Typ  Max  Condition
        #       0    0    0    sensor in open air
        #       0    20   300  sensor in dry soil
        #       300  580  700  sensor in humid soil
        #       700  940  950  sensor in water

        level = math.ceil(value * 10 / 700)

        # Optimize Level between 1 and 10:
        if level < 1:
            level = 1
        if level > 10:
            level = 10

        grovepi.ledBar_setLevel(self.led_bar, level)

    def run_test(self):
        print('run test for led-bar: ')

        # LED Bar methods
        # grovepi.ledBar_init(pin,orientation)
        # grovepi.ledBar_orientation(pin,orientation)
        # grovepi.ledBar_setLevel(pin,level)
        # grovepi.ledBar_setLed(pin,led,state)
        # grovepi.ledBar_toggleLed(pin,led)
        # grovepi.ledBar_setBits(pin,state)
        # grovepi.ledBar_getBits(pin)

        try:
            # ledbar_init(pin, orientation)
            # orientation: (0 = red to green, 1 = green to red)
            grovepi.ledBar_init(self.led_bar, 1)
            time.sleep(.5)

            for i in range(0, 11):
                grovepi.ledBar_setLevel(self.led_bar, i)
                time.sleep(.1)

            time.sleep(1)

            grovepi.ledBar_init(self.led_bar, 0)

            for i in range(0, 11):
                grovepi.ledBar_setLevel(self.led_bar, i)
                time.sleep(.1)

            time.sleep(1)

            grovepi.ledBar_setLevel(self.led_bar, 0)
            grovepi.ledBar_init(self.led_bar, 0)

            print('output-test was successful.')

        except KeyboardInterrupt:
            print('Output: Keyboard Interrupt')
            grovepi.ledBar_setBits(self.led_bar, 0)

        except IOError:
            print('OutputError: LED-Bar not working.')