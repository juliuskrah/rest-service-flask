from flask_restful import abort
from datetime import datetime

TODOS = [
    {'id': 1, 'description': 'Create a post on REST using Flask',
        'created_time': str(datetime.now()), 'modified_time': None},
    {'id': 2, 'description': 'Store REST data in a database for Flask post',
        'created_time': str(datetime.now()), 'modified_time': None},
    {'id': 3, 'description': 'Secure a REST service in Flask',
        'created_time': str(datetime.now()), 'modified_time': None},
    {'id': 4, 'description': 'Write another article on Flask',
        'created_time': str(datetime.now()), 'modified_time': None},
    {'id': 5, 'description': 'Secure a flask REST service using JWT',
        'created_time': str(datetime.now()), 'modified_time': None},
    {'id': 6, 'description': 'Secure a REST service in Flask using OAuth2',
        'created_time': str(datetime.now()), 'modified_time': None},
    {'id': 7, 'description': 'SQL Migration using Flask',
        'created_time': str(datetime.now()), 'modified_time': None},
    {'id': 8, 'description': 'Write a flask tutorial for WebSockets',
        'created_time': str(datetime.now()), 'modified_time': None},
    {'id': 9, 'description': 'Form handling in Flask',
        'created_time': str(datetime.now()), 'modified_time': None},
    {'id': 10, 'description': 'Handling binary files in flask',
        'created_time': str(datetime.now()), 'modified_time': None},
]


def remove_todo(key):
    """
    Delete a Dictionary from an Array
    """
    todo = find_todo(key)
    TODOS.remove(todo)


def update_todo(todo, key):
    """
    Update a Dictionary in an Array
    """
    for idx, item in enumerate(TODOS):
        if key is item['id']:
            todo['id'] = key
            todo['modified_time'] = str(datetime.now())
            todo['created_time'] = item['created_time']
            TODOS[idx] = todo


def add_todo(todo):
    """
    Add a Dictionary to an Array
    """
    # TODO set id on create todo['id'] = increment
    todo['created_time'] = str(datetime.now())
    TODOS.append(todo)


def find_todo(key):
    """
    Search function that searches for a Dictionary within an Array
    """
    return next((item for item in TODOS if item["id"] == key), None)


def abort_if_todo_doesnt_exist(todo_id):
    if find_todo(todo_id) is None:
        abort(404, message="Todo {} doesn't exist".format(todo_id))
