import imp
import os
from flask import Flask, jsonify, request, abort
from models import setup_db, Greeting
from flask_cors import CORS
from auth import requires_auth
Page_count = 10
# this is for test

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "hi"
        if excited == 'true':
            greeting = greeting + "!!!!! You are doing great in this Udacity project."
        return greeting

    @app.route('/', methods=['GET'])
    def index():
        return "<h1>hello friends</h1>"

    @app.route('/greetings', methods=['GET'])
    @requires_auth(["get:greetings"])
    def greeting_all(payload):
        page = request.args.get('page', 1, type=int)
        pagination = Greeting.query.paginate(
            page, per_page=Page_count, error_out=False)
        greetings = pagination.items
        # TODO implement pagination
        # greetings = Greeting.query.all()
        greetings = [greeting.format() for greeting in greetings]
        return jsonify({'greetings': greetings, 'count': pagination.total})

    @app.route('/greetings/<lang>', methods=['GET'])
    @requires_auth(["get:greetings"])
    def greeting_one(payload, lang):
        greeting = Greeting.query.filter_by(lang=lang).first()
        print(lang)
        # if(lang not in greetings):
        if(not greeting):
            abort(404)
        return jsonify({'greeting': greeting.format()})

    @app.route('/greetings', methods=['POST'])
    @requires_auth(["post:greetings"])
    def greeting_add(payload):
        info = request.get_json()
        if('lang' not in info or 'greeting' not in info):
            abort(422)
        # greetings[info['lang']] = info['greeting']
        greeting = Greeting(info['lang'], info['greeting'])
        greeting.insert()
        return jsonify({'greeting': greeting.format()}), 201

    # TODO: implement beautifull greeting
    @app.route('/greetings/<lang>/beautiful', methods=['POST'])
    def beautiful_greeting(payload, lang):
        greeting = "namastai"
        return jsonify({'greeting': f'greeting in language {lang} is {greeting}'})

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
        }), 422

    @app.errorhandler(404)
    def unprocessable(error):
        return jsonify({
            "message": "resource not found",
            "success": False,
            "error": 404,
        }), 404

    @app.errorhandler(401)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 401,
        }), 401

    @app.errorhandler(403)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 403,
        }), 403

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
