from flask_restplus import Resource, Namespace
from flask import request, jsonify
from app.api.utils.tasks import *

from werkzeug.exceptions import BadRequest

api = Namespace('task', description='Operations related to task management and organization')

task_sets = {'Default': TaskSet([Task('default_task', details='A default task')])}


@api.route('<string:task_set_id>')
class Task(Resource):

    def get(self, task_set_id):
        """Retrieve the list of tasks in set with specified id"""
        return task_sets.get(task_set_id, [])

    def post(self, task_set_id):
        """Add a new task to a task set with specified id"""
        name = request.json['name']
        details = request.json['details']

        task_set = task_sets.get(task_set_id)

        if not task_set:
            return BadRequest(f'Could not find a task set under the id {task_set_id}')
        else:
            task_set.tasks.append(Task(name, details))
            return jsonify(success=True)
