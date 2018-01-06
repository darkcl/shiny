
from flask import Flask
from flask import render_template, jsonify

from core import *

def start_web(path):
    """Start Web Server"""

    app = Flask(__name__, template_folder='templates')

    @app.route("/")
    def home():
        return render_template('react.html')
    
    @app.route("/pokemon", methods=['GET', 'POST'])
    def list_pokemon():
        if request.method == 'GET':
            d = list_info_model(path)
            return jsonify(d)
        else:
            return 'Under Construction'

    @app.route("/pokemon/<pokemon_id>")
    def show_pokemon(pokemon_id):
        d = list_info_model(path, str(pokemon_id))
        return jsonify(d)

    @app.route("/pokemon/<pokemon_id>/add")
    def encounter_pokemon(pokemon_id):
        add_counter_id(str(pokemon_id), path)
        d = list_info_model(path, str(pokemon_id))
        return jsonify(d)

    return app
