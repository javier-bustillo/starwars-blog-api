"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Favorite
import json

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/users', methods=['GET'])
def get_all_users():

    users = User.query.all()
    users_list = list(map(lambda x: x.serialize(), users))

    response_body = {
        "results": users_list
    }

    return jsonify(response_body), 200


@app.route('/people', methods=['GET'])
def get_all_characters():

    all_characters = Character.query.all()
    all_characters_list = list(map(lambda x: x.serialize(), all_characters))

    response_body = {
        "results": all_characters_list
    }

    return jsonify(response_body), 200


@app.route('/planets', methods=['GET'])
def get_all_planets():

    all_planets = Planet.query.all()
    all_planets_list = list(map(lambda x: x.serialize(), all_planets))

    response_body = {
        "results": all_planets_list
    }

    return jsonify(response_body), 200


@app.route('/people/<int:id>', methods=['GET'])
def get_people_by_id(id):

    people_by_id = Character.query.filter_by(id=id).first_or_404(
        description='There is no data with people id: {}'.format(id))

    response_body = {
        "results": people_by_id.serialize()
    }

    return jsonify(response_body), 200


@app.route('/planets/<int:id>', methods=['GET'])
def get_planets_by_id(id):

    planets_by_id = Planet.query.filter_by(id=id).first_or_404(
        description='There is no data with planet id: {}'.format(id))

    response_body = {
        "results": planets_by_id.serialize()
    }

    return jsonify(response_body), 200


@app.route('/users/favorites/<int:user_id>', methods=['GET'])
def get_all_users_favorites(user_id):

    favorites = Favorite.query.filter_by(user_id=user_id)
    favorites_list = list(map(lambda x: x.serialize(), favorites))

    response_body = {
        "results": favorites_list
    }

    return jsonify(response_body), 200


@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def create_new_planet_to_current_user(planet_id):

    body = json.loads(request.data)

    create_planet_request = Favorite(
        user_id=body['user_id'], planet_id=planet_id)
    db.session.add(create_planet_request)
    db.session.commit()

    response_body = {
        "msg": "Planet Created"
    }

    return jsonify(response_body), 200


@app.route('/favorite/people/<int:character_id>', methods=['POST'])
def create_new_character_to_current_user(character_id):

    body = json.loads(request.data)

    create_character_request = Favorite(
        user_id=body['user_id'], character_id=character_id)
    db.session.add(create_character_request)
    db.session.commit()

    response_body = {
        "msg": "Character Created"
    }

    return jsonify(response_body), 200


@app.route('/favorite/<int:user_id>/people/<int:character_id>', methods=['DELETE'])
def delete_character_in_current_user(user_id, character_id):

    delete_character_query = Favorite.query.filter_by(
        user_id=user_id).filter_by(character_id=character_id).first()
    db.session.delete(delete_character_query)
    db.session.commit()

    response_body = {
        "msg": "Character Deleted"
    }

    return jsonify(response_body), 200


@app.route('/favorite/<int:user_id>/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet_in_current_user(user_id, planet_id):

    delete_planet_query = Favorite.query.filter_by(
        user_id=user_id).filter_by(planet_id=planet_id).first()
    db.session.delete(delete_planet_query)
    db.session.commit()

    response_body = {
        "msg": "Planet Deleted"
    }

    return jsonify(response_body), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
