from flask import Flask
from GPIOControler import GPIOController

class HTTPReceiver:

    def __init__(self):
        # Setup GPIOw
        self.gipoControler = GPIOController()
        self.app = Flask(__name__)
        self.activated = False
        self.add_routes()

    def add_routes(self):
        # define the rules and links to make with
        self.app.add_url_rule('/gpio/onoff', 'lights_on_off', self.lights_on_off)
        self.app.add_url_rule('/gpio/light_blue', 'activate_light_blue_lights', self.activate_light_blue_lights)
        self.app.add_url_rule('/gpio/medium_blue', 'activate_medium_blue_lights', self.activate_medium_blue_lights)
        self.app.add_url_rule('/gpio/dark_blue', 'activate_dark_blue_lights', self.activate_dark_blue_lights)
        self.app.add_url_rule('/gpio/green', 'activate_green_lights', self.activate_green_lights)
        self.app.add_url_rule('/gpio/orange', 'activate_orange_lights', self.activate_orange_lights)
        self.app.add_url_rule('/gpio/red', 'activate_red_lights', self.activate_red_lights)

    def start_listening_http(self):
        self.app.run(host='0.0.0.0', port=5000)
        self.activated = True

    def lights_on_off(self):
        self.gipoControler.lights_on_off()
        return "light turned on/off"

    def activate_light_blue_lights(self):
        self.gipoControler.activate_light_blue_lights()
        return "light blue light turned on"

    def activate_medium_blue_lights(self):
        self.gipoControler.activate_medium_blue_lights()
        return "medium blue light turned on"

    def activate_dark_blue_lights(self):
        self.gipoControler.activate_dark_blue_lights()
        return "dark blue light turned on"

    def activate_green_lights(self):
        self.gipoControler.activate_green_lights()
        return "green light turned on"

    def activate_orange_lights(self):
        self.gipoControler.activate_orange_lights()
        return "orange light turned on"

    def activate_red_lights(self):
        self.gipoControler.activate_red_lights()
        return "red light turned on"
