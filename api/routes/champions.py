from flask import Blueprint, jsonify
import json
from ..helpers.convert_name import convert_name
from ..models.champions import Champions
from ..models.champion_stats import Stats

BASE = r'http://127.0.0.1:5000/'

champions = Blueprint('champions', __name__)

@champions.route('/', methods=['GET'])
def get_all_champs():
    champions = Champions().read_all_champs()
    response = {
        "champs": champions, 
        "status": 200,
        "links": {"self": BASE + "champions", "champ_stats": BASE + "champions/<name>/<stars>/<rank>"},
        "message": "OK"
        }
    return response, 200

@champions.route('/<name>/<stars>/<rank>', methods=['GET'])
def get_champ_stats(name, stars, rank):

    champ_name = convert_name(name)

    stats = Stats()
    champ_stats = stats.read_champ_stats(champ_name, stars, rank)
    
    response = {
        "champ_name": champ_name,
        "champ_stats": champ_stats,
        "status": 200,
        "message": "OK"
    }
    return response, 200
