from flask import Blueprint, redirect, render_template, request
from flask_restful import Api, Resource


blueprint = Blueprint(__name__, __name__)
api = Api(blueprint)


@api.resource('/oauth')
class Oauth(Resource):
    def get(self):
        code = str(request.args.get('code'))
        return str(code)