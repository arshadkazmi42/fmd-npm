import sys
import requests
import time

from random import randrange



NPM_URL = 'https://www.npmjs.com/package/'



def _get_url_arg():
    args = sys.argv

    if len(args) < 2:
        print('Missing URL!')
        exit()

    return args[1]

def _call_api(url):

    response = requests.get(url)

    if response.status_code != 200:
        print(f'Failed with error code {response.status_code}')
        return {}
        
    return response.json()


url = _get_url_arg()
result = _call_api(url)

dependencies = []

if result and 'dependencies' in result:
    dependencies = result['dependencies']

    for name, value in dependencies.items():
        print(f'{NPM_URL}{name}')

