from flask_restful import Resource
from flask import request
from todoapi.common import util

class Todo(Resource):
    def get(self, todo_id):
        """
        GET /api/v1.0/resources/:todo_id
        """
        util.abort_if_todo_doesnt_exist(todo_id)
        return util.find_todo(todo_id)

    def delete(self, todo_id):
        """
        DELETE /api/v1.0/resources/:todo_id
        """
        util.abort_if_todo_doesnt_exist(todo_id)
        util.remove_todo(todo_id)
        return '', 204

    def put(self, todo_id):
        """
        PUT /api/v1.0/resources/:todo_id
        """
        util.abort_if_todo_doesnt_exist(todo_id)
        task = request.get_json(force=True)
        util.update_todo(task, todo_id)
        return task, 201

class TodoList(Resource):
    def get(self):
        """
        GET /api/v1.0/resources/
        """
        return util.TODOS

    def post(self):
        """
        POST /api/v1.0/resources/:todo_id
        """
        # TODO return Location header
        task = request.get_json(force=True)
        util.add_todo(task)
        return task, 201
