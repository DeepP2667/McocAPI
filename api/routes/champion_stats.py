from flask import Blueprint, request
import json
from ..helpers.convert_name import convert_name
from ..models.champions import Champions
from ..models.champion_stats import Stats

champion_stats = Blueprint("champion_stats", __name__)


def invalid_parms(stats):
    if stats == None or stats == []:
        response = {
            "title": "Invalid parameters",
            "message": "Parameters must be integers and must within range",
            "help": "https://github.com/DeepP2667/McocAPI/blob/master/stars_rank.md",
            "code": 400,

        }
        return response

@champion_stats.route('/<name>', methods=['GET'])
def get_all_stats(name):
    try:
        champ_name = convert_name(name)
    except KeyError as e:
        print(e)
        response_all_stats = {
            "error": {
                "title": "Invalid name",
                "help": "https://github.com/DeepP2667/McocAPI/blob/master/api_champ_names.md",
                "message": f"Name {e} not found",
                "code": 404,
            }
        }
        return response_all_stats, 404

    champ = Champions()
    base_champ_stats = champ.read_base_champ_stats(champ_name)[0]

    stats = Stats()
    champ_stats = stats.read_all_champ_stats(champ_name)

    resonse_all_stats = {
                    "champ_name": champ_name,
                    "champ_id": base_champ_stats['champ_id'],
                    "champ_class": base_champ_stats['champ_class'],
                    "champ_offense_rank": base_champ_stats['offense_rank'],
                    "champ_defense_rank": base_champ_stats['defense_rank'],
                    "champ_stats": champ_stats,
                    "status": 200,
                    "message": "OK"
                }

    return resonse_all_stats, 200

@champion_stats.route('/<name>/', methods=['GET'])
def get_specific_stats(name):

    stars = request.args.get('stars')
    rank = request.args.get('rank')
    try:
        champ_name = convert_name(name)
    except KeyError as e:
        print(e)
        response_all_stats = {
            "error": {
                "title": "Invalid name",
                "message": f"Name {e} not found",
                "code": 404,
            }
        }
        return response_all_stats, 404

    champ = Champions()
    base_champ_stats = champ.read_base_champ_stats(champ_name)[0]

    stats = Stats()
    specific_stats = stats.read_specific_champ_stats(champ_name, stars, rank)

    invalid_response = invalid_parms(specific_stats)

    if invalid_response != None:
        return invalid_response, invalid_response['code']

    response_stats = {
        "champ_name": champ_name,
        "champ_class": base_champ_stats['champ_class'],
        "champ_offense_rank": base_champ_stats['offense_rank'],
        "champ_defense_rank": base_champ_stats['defense_rank'],
        "champ_stats": specific_stats,
        "status": 200,
        "message": "OK"
    }
    
    return response_stats, 200
