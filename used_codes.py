import json
import os

def read_codes(game='Borderlands 2', platform='PC'):
    '''
    Returns a list of all the codes of the specified game that have already been used.
    '''
    if not (os.path.exists("used_codes.json")):
        create_json()
        
    codeList = []

    with open('used_codes.json', 'r') as json_file:  
        codes = json.load(json_file)
        codeList = codes[game][platform]

    return codeList

def write_codes(code, game='Borderlands 2', platform='PC'):
    '''
    Adds a code to the json file.
    '''
    if not (os.path.exists("used_codes.json")):
        create_json()

    codes = {}

    with open('used_codes.json', 'r') as json_file:  
        codes = json.load(json_file)
    
    if (code not in codes[game][platform]):
        codes[game][platform].append(code)

        with open('used_codes.json', 'w') as json_file:  
            json.dump(codes, json_file)
    
def create_json():
    '''
    Creates a new JSON file with the required layout.
    '''
    data = {}

    data['Borderlands 1'] = {
        'PC': [],
        'PS4': [],
        'xBox': []
    }

    data['Borderlands 2'] = {
        'PC': [],
        'PS4': [],
        'xBox': []
    }

    data['Borderlands - Pre Sequel'] = {
        'PC': [],
        'PS4': [],
        'xBox': []
    }

    data['Borderlands 3'] = {
        'Multi': []
    }

    data['VIP'] = {
        'Multi': []
    }

    with open('used_codes.json', 'w') as outfile:
        json.dump(data, outfile)
