from light import Light
from launcher import Launcher

import time
import env

def main():
    launcher = Launcher(env.STOCK_SYMBOL)
    launcher.synchronize_stock_price_and_light(env.POLLING_SECONDS)

if __name__ == "__main__":
    main()