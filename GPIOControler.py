import time

class GPIOController:
    def __init__(self):
        print("init")
        # Setup GPIO
        # GPIO.setmode(GPIO.BCM)
        # add all used GPIO's here
        # GPIO.setup(18, GPIO.OUT)

    def lights_on_off(self):
        print("on off Light")
        self.activate_light(17)

    def activate_light_blue_lights(self):
        print("light blue light")
        self.activate_light(17)

    def activate_medium_blue_lights(self):
        print("medium blue light")
        self.activate_light(17)

    def activate_dark_blue_lights(self):
        print("dark blue light")
        self.activate_light(17)

    def activate_green_lights(self):
        print("green light")
        self.activate_light(17)

    def activate_orange_lights(self):
        print("blue light")
        self.activate_light(17)

    def activate_red_lights(self):
        print("red light")
        self.activate_light(17)

    def activate_light(self, number):
        # GPIO.output(number, GPIO.HIGH)
        time.sleep(0.5)
        # GPIO.output(number, GPIO.LOW)