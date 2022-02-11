import json

def convert_to_api_name(name):

    with open('api_champ_names.json', 'r') as file:
        data = json.load(file)

    temp = name.replace('(', '')
    temp = temp.replace(')', '')
    temp = temp.replace(' ', '-')
    temp = temp.lower()
    temp = temp.strip()

    data['api_champ_names'][temp] = name
    data['champ_count'] = data['champ_count'] + 1

    with open('api_champ_names.json', 'w') as file:
        data = json.dump(data, file, indent=4)


def convert_name(api_name):
    with open('api_champ_names.json', 'r') as file:
        data = json.load(file)
        champ_name = data['api_champ_names'][api_name]

    return champ_name