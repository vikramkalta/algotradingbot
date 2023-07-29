from common import constants 
from external_requests import get

def get_balances():
    url = constants.BASE_URL + 'v3/accounts/' + constants.ACCOUNT_ID + '/summary'
    response_text = get.make_get_request(url=url)
    return response_text
