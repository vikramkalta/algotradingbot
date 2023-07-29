import time
from market_operations import market_price, order
from common import constants

is_next_operation_buy = True
last_op_price = 100.00

def start_bot():
    while True:
        attempt_to_make_trade()
        # Add a 1-second delay before next iteration
        time.sleep(300)

def attempt_to_make_trade():
    currentPrice = market_price.get_market_price()
    percentageDiff = (currentPrice - last_op_price) / last_op_price * 100
    if  is_next_operation_buy:
        try_to_buy()
    else:
        try_to_sell()

def try_to_buy(percentage_diff):
    if percentage_diff >= constants.UPWARD_TREND_THRESHOLD or percentage_diff <= constants.DIP_THRESHOLD:
        last_op_price = order.place_buy_order()
        is_next_operation_buy = False

def try_to_sell(percentage_diff):
    if percentage_diff >= constants.PROFIT_THRESHOLD or percentage_diff <= constants.STOP_LOSS_THRESHOLD:
        last_op_price = order.place_sell_order()
        is_next_operation_buy = True