from simplexml import dumps
from flask import make_response, Flask
from flask_restful import Api
from todoapi.resources import todo_resource


def output_xml(data, code, headers=None):
    """Makes a Flask response with a XML encoded body"""
    resp = make_response(dumps({'response': data}), code)
    resp.headers.extend(headers or {})
    return resp


app = Flask(__name__)
api = Api(app, default_mediatype='application/json')
api.representations['application/xml'] = output_xml

api.add_resource(todo_resource.TodoList, '/api/v1.0/resources/')
api.add_resource(todo_resource.Todo, '/api/v1.0/resources/<int:todo_id>')
