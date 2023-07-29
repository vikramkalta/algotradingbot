from common import constants 
from external_requests import post, get

def place_sell_order():
    url = constants.BASE_URL + 'v3/accounts/' + constants.ACCOUNT_ID + '/orders'
    data = {
        'order': {
            'units': '-10',
            'instrument': 'EUR_USD',
            'timeInForce': 'FOK',
            'type': 'MARKET',
            'positionFill': 'DEFAULT'
        }
    }
    response_text = post.make_post_request(url=url, data=data)
    return response_text

def place_buy_order():
    url = constants.BASE_URL + 'v3/accounts/' + constants.ACCOUNT_ID + '/orders'
    data = {
        'order': {
            'units': '10',
            'instrument': 'EUR_USD',
            'timeInForce': 'FOK',
            'type': 'MARKET',
            'positionFill': 'DEFAULT'
        }
    }
    response_text = post.make_post_request(url=url, data=data)
    return response_text

def get_order_details(id):
    url = constants.BASE_URL + 'v3/accounts/' + constants.ACCOUNT_ID + '/orders' + id
    response_text = get.make_get_request(url=url)
    return response_text
