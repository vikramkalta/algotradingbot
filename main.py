from market_operations import balances, market_price

def main():
    # url = 'https://api-fxpractice.oanda.com/v3/accounts/101-004-26396988-001/orders'
    # data = {
    #     'order': {
    #         'units': '10',
    #         'instrument': 'EUR_USD',
    #         'timeInForce': 'FOK',
    #         'type': 'MARKET',
    #         'positionFill': 'DEFAULT'
    #     }
    # }
    # headers = {'Authorization': 'Bearer 7d513675f2cee83e8422c43509bf7b1a-612622c8422ca59ce89f247233b199db',
    #            'Content-Type': 'application/json'}
    # response_text = post.make_post_request(url, data, headers=headers)
    # if response_text:
    #     print('Response:', response_text)
    # test = get_balances.get_balances()
    test = market_price.get_market_price()
    print('test', test)

if __name__ == '__main__':
    main()
