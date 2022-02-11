from flask import Blueprint, jsonify
import json
from ..helpers.convert_name import convert_name
from ..models.champions import Champions
from ..models.champion_stats import Stats


champion_stats = Blueprint("champion_stats", __name__)


@champion_stats.route('/<name>', methods=['GET'])
def get_all_stats(name):

    champ_name = convert_name(name)

    champ = Champions()
    base_champ_stats = champ.read_base_champ_stats(champ_name)[0]

    stats = Stats()
    champ_stats = stats.read_all_champ_stats(champ_name)

    final_stats = {
                    "champ_name": champ_name,
                    "champ_id": base_champ_stats['champ_id'],
                    "champ_class": base_champ_stats['champ_class'],
                    "champ_offense_rank": base_champ_stats['offense_rank'],
                    "champ_defense_rank": base_champ_stats['defense_rank'],
                    "champ_stats": champ_stats,
                    "status": 200,
                    "message": "OK"
                }

    return final_stats, 200

@champion_stats.route('/<name>/<stars>/<rank>', methods=['GET'])
def get_specific_stats(name, stars, rank):

    champ_name = convert_name(name)

    champ = Champions()
    base_champ_stats = champ.read_base_champ_stats(champ_name)[0]

    stats = Stats()
    specific_stats = stats.read_specific_champ_stats(champ_name, stars, rank)
    
    response = {
        "champ_name": champ_name,
        "champ_class": base_champ_stats['champ_class'],
        "champ_offense_rank": base_champ_stats['offense_rank'],
        "champ_defense_rank": base_champ_stats['defense_rank'],
        "champ_stats": specific_stats,
        "status": 200,
        "message": "OK"
    }
    return response, 200
