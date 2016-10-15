import os
from flask import Flask, url_for, request, jsonify
from flask_restful import Resource, Api

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '\x87\x95\xaa\x86\x16*3n&x\x85PgY\xc4\xc3\xddl\x05\xad\xa7\x9a(\xd4'

api = Api(app)

# Register BluePrints
from baseviews.views import baseviews
app.register_blueprint(baseviews)

from apis.confapis import confapis
app.register_blueprint(confapis)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
