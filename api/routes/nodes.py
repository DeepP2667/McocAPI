from flask import Blueprint
from api.models.nodes import Nodes

nodes = Blueprint('nodes', __name__)

BASE = r'http://127.0.0.1:5000/'

@nodes.route('/', methods=['GET'])
def get_nodes():
    nodes = Nodes.read_nodes()
    response_nodes = {"nodes": [],
                      "status": 200,
                      "message": "OK",
                      "links": {"node": BASE + "<node_id>", "source": "https://www.dunres.sk/mcoc/buffs/"}
                      }
    response_nodes['nodes'] = nodes

    return response_nodes, 200