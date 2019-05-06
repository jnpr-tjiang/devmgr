from flask import Blueprint
from flask_restful import Api

from devmgr.api.resources import DeviceResource, DeviceList

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

api.add_resource(DeviceResource, '/devices/<int:device_id>')
api.add_resource(DeviceList, '/devices')
