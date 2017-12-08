from flask_restful import abort

TODOS = {
    'todo1': {'task': 'Create a post on REST using Flask'},
    'todo2': {'task': 'Store REST data in a database for Flask post'},
    'todo3': {'task': 'Secure a REST service in Flask'},
}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))
