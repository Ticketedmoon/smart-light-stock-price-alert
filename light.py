import logging
from yeelight import discover_bulbs, Bulb, LightType, BulbException
from random import randrange

logging.basicConfig(level = logging.INFO)

class Light: 

    IP_ADDRESS = "192.168.0.150"

    def __init__(self):
        self.bulb = Bulb(self.IP_ADDRESS)
        try: 
            self.turn_on()
        except BulbException:
            logging.info(f"Bulb [{self.IP_ADDRESS}] is already active.")

    def turn_on(self):
        self.bulb.turn_on()
    
    def turn_off(self):
        self.bulb.turn_off()
    
    def toggle(self):
        self.bulb.toggle()
        
    def set_brightness(self, brightness):
        self.bulb.set_brightness(brightness) # (%)

    def set_brightness_with_type(self, brightness, light_type=None):
        if (light_type != None):
            self.bulb.set_brightness(brightness, light_type=light_type)
        else:
            self.bulb.set_brightness(brightness, light_type=LightType.Ambient)

    def set_rgb(self, r, g, b):
        self.bulb.set_rgb(r, g, b)
    
    def set_hsv(self, h, s, v):
        self.bulb.set_hsv(h, s, v)

    def set_hsv_without_brightness(self, h, s):
        self.bulb.set_hsv(h, s)

    def set_color_temp(self, temp):
        self.bulb.set_color_temp(temp)

    def save_setting_as_default(self):
        self.bulb.set_default()

    def set_random_rgb_color(self):
        r = randrange(255)
        g = randrange(255)
        b = randrange(255)
        self.set_rgb(r, g, b)