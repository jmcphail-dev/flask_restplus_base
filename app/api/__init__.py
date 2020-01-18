from flask import Blueprint
from flask_restplus import Api

from app.api.controller.task_controller import api as task_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Flask-RESTPlus Sample application',
          version='1.0',
          desription='A sample to showcase Flask-RESTPlus functionality within a small web service'
          )

api.add_namespace(task_ns)