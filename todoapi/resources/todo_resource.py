from flask_restful import Resource, reqparse
from todoapi.common import util

TODOS = {
    'todo1': {'task': 'Create a post on REST using Flask'},
    'todo2': {'task': 'Store REST data in a database for Flask post'},
    'todo3': {'task': 'Secure a REST service in Flask'},
}

parser = reqparse.RequestParser()
parser.add_argument('task')

class Todo(Resource):
    def get(self, todo_id):
        util.abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        util.abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201
