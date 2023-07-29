import requests
from common import constants

def make_delete_request(url, headers=None):
    try:
        headers = {'Authorization': 'Bearer ' + constants.AUTH_TOKEN,
               'Content-Type': 'application/json'}
        response = requests.delete(url=url, headers=headers)
        if response.status_code >= 200 and response.status_code < 400:
            print('Request was successful')
            return response.text
        else:
            print('Request failed with status code:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('An error occurred:', e)
        return None