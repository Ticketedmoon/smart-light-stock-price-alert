import logging
import logging

from stock_checker import StockChecker
from light import Light
from yeelight import BulbException

from apscheduler.schedulers.background import BlockingScheduler

logging.basicConfig(level = logging.INFO)

class Launcher:

    current_stock_price = -1

    def __init__(self, stock_symbol):
        self.stock_checker = StockChecker(stock_symbol)
        self.light = Light()
        self.schedular = BlockingScheduler()

    def synchronize_stock_price_and_light(self, seconds):
        # Will call method every X seconds
        self.schedular.add_job(self.__update_lights_when_stock_changes, 'interval', seconds=seconds)
        self.schedular.start()

    def __update_lights_when_stock_changes(self):
        logging.info("Checking stocks for signicant change - synchronising connected light...")
        updated_stock_price = self.stock_checker.get_stock_price()
        if updated_stock_price != self.current_stock_price:
            try:
                if updated_stock_price > self.current_stock_price:
                    self.light.set_rgb(0, 255, 0)
                else:
                    self.light.set_rgb(255, 0, 0)
            except BulbException:
                logging.warn("Something went wrong with YeeLight connected...")