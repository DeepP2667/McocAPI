from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

    from .routes.champions import champions
    from .routes.champion_stats import champion_stats
    from .routes.nodes import nodes

    app.register_blueprint(champions, url_prefix='/champions')
    app.register_blueprint(champion_stats, url_prefix='/champions')
    app.register_blueprint(nodes, url_prefix='/nodes')

    return app