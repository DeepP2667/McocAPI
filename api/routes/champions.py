from flask import Blueprint, jsonify
import json
from ..helpers.convert_name import convert_name
from ..helpers.read_names import read_api_names

BASE = r'http://127.0.0.1:5000/'

champions = Blueprint('champions', __name__)

@champions.route('/', methods=['GET'])
def get_all_champs():
    names = read_api_names()
    response = {
        "champs": names['api_champ_names'], 
        "links": {"self": BASE + "champions", 
                  "champ_stats": BASE + "champions/<name>/<stars>/<rank>", 
                  "source": "https://auntm.ai/"},
        "status": 200,
        "message": "OK"
        }
    return response, 200

