from simplexml import dumps
from flask import make_response, Flask
from flask_restful import Resource, Api
from todoapi.resources import todo_resource

TODOS = {
    'todo1': {'task': 'Create a post on REST using Flask'},
    'todo2': {'task': 'Store REST data in a database for Flask post'},
    'todo3': {'task': 'Secure a REST service in Flask'},
}

def output_xml(data, code, headers=None):
    """Makes a Flask response with a XML encoded body"""
    resp = make_response(dumps({'response': data}), code)
    resp.headers.extend(headers or {})
    return resp

app = Flask(__name__)
api = Api(app, default_mediatype='application/json')
api.representations['application/xml'] = output_xml

class HelloWorld(Resource):
    def get(self):
        return TODOS

api.add_resource(HelloWorld, '/api/v1.0/resources')
api.add_resource(todo_resource.Todo, '/api/v1.0/resources/<string:todo_id>')
