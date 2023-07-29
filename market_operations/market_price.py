from common import constants
from external_requests import get
from urllib.parse import urlencode, quote

def get_market_price():
    instruments = ['EUR_USD', 'USD_CAD']
    # Convert the array elements into URL-encoded strings
    encoded_instruments = [quote(instrument) for instrument in instruments]
    # Join the encoded instruments with commas
    instruments_query = ','.join(encoded_instruments)
    # Using a dictionary to create the query params
    params_dict = { 'instruments': instruments_query }
    query_string = urlencode(params_dict)
    url = constants.BASE_URL + 'v3/accounts/' + \
        constants.ACCOUNT_ID + '/pricing?' + query_string
    response_text = get.make_get_request(url=url)
    return response_text
