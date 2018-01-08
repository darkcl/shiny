
from flask import Flask
from flask import render_template, jsonify, request
from flask import Response

from core import *

def start_web(path):
    """Start Web Server"""

    app = Flask(__name__, template_folder='templates')

    @app.route("/")
    def home():
        d = list_info_model(path)
        return render_template('index.html', entries=d)

    @app.route("/counter/<pokemon_id>")
    def counter_home(pokemon_id):
        d = list_info_model(path, str(pokemon_id))
        return render_template('counter.html', id=pokemon_id, entry=d)
    
    @app.route("/api/pokemon", methods=['GET', 'POST'])
    def list_pokemon():
        if request.method == 'GET':
            d = list_info_model(path)
            return jsonify(d)
        elif request.method == 'POST':
            body = request.get_json()
            if "name" in body:
                return (Response(status=200) if create_hunt(body["name"], path) else Response(status=403))
            else:
                return Response(status=403)
        else:
            return 'Under Construction'

    @app.route("/api/pokemon/<pokemon_id>")
    def show_pokemon(pokemon_id):
        d = list_info_model(path, str(pokemon_id))
        return jsonify(d)

    @app.route("/api/pokemon/<pokemon_id>/add")
    def encounter_pokemon(pokemon_id):
        add_counter_id(str(pokemon_id), path)
        d = list_info_model(path, str(pokemon_id))
        text_path = os.path.join(os.getcwd(), "{}.txt".format(d["name"]))
        export_text_progress(d["name"], path, text_path)
        return jsonify(d)

    @app.route("/api/pokemon/<pokemon_id>/completed")
    def complete_hunt(pokemon_id):
        mark_done_id(str(pokemon_id), path)
        d = list_info_model(path, str(pokemon_id))
        return jsonify(d)

    return app
