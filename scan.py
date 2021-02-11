import requests
import time
from random import randrange
import json

NPM_URL = 'https://www.npmjs.com/package/'
MODES = {
    'FILE': 'file',
    'URL': 'url'
}


# Change your Mode
# MODES['FILE'] => If you want to scan files
# MODES['URL'] => If you want to scan urls
CURRENT_MODE = MODES['FILE']

URLs = []                       # Comma separated string of URLs
FILEs = ['package.json']        # Comma separated string of absolute file paths



def _get_url_result(url):

    response = requests.get(url)

    if response.status_code != 200:
        print(f'Failed with error code {response.status_code}')
        return {}
        
    return response.json()

def _get_file_result(path):

    with open(path) as f:
        result = json.load(f)
    
    return result


data = []
if CURRENT_MODE == MODES['URL']:
    data = URLs
elif CURRENT_MODE == MODES['FILE']:
    data = FILEs

for value in data:

    print('\n\n')
    print('---------------------------')
    print('Current Settings')
    print(f'Mode: {CURRENT_MODE}')
    print(f'Value: {value}')
    print('---------------------------')
    print('\n\n')

    if CURRENT_MODE == MODES['URL']:
        result = _get_url_result(value)
    elif CURRENT_MODE == MODES['FILE']:
        result = _get_file_result(value)

    name = result['name']
    dependencies = {}
    
    if 'dependencies' in result:
        dependencies = result['dependencies']

    broken_dependencies = []
    for name, value in dependencies.items():
        print(f'Processing: ', name)
        try:
            response = requests.get(f'{NPM_URL}{name}')
            
            if (response.status_code == 404):
                broken_dependencies.append(value)

                print('----------BROKEN----------')
                print(f'Name: {name}')
                print(f'Version: {value["version"]}')
                print('----------BROKEN----------')
        except:
            print(f'Error processing: ', name)

        rand = randrange(5)
        time.sleep(rand)

    print(str(broken_dependencies))
