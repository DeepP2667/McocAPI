import json

def read_api_names():

    with open('api_champ_names.json', 'r') as file:
        data = json.load(file)

    return data