from flask import request
from flask_restful import Resource

from devmgr.models import Device
from devmgr.extensions import ma, db
from devmgr.common.pagination import paginate


class DeviceSchema(ma.ModelSchema):
    class Meta:
        model = Device
        sqla_session = db.session


class DeviceResource(Resource):
    """Single device resource
    """

    def get(self, device_id):
        schema = DeviceSchema()
        device = Device.query.get_or_404(device_id)
        return {
            'device': schema.dump(device).data
        }

    def put(self, device_id):
        schema = DeviceSchema()
        device = Device.query.get_or_404(device_id)
        device, errors = schema.load(request.json, instance=device)
        if errors:
            return errors, 422

        db.session.commit()

        return {
            'msg': 'device updated',
            'device': schema.dump(device).data
        }

    def delete(self, device_id):
        device = Device.query.get_or_404(device_id)
        db.session.delete(device)
        db.session.commit()

        return {
            'msg': "Device (%s) deleted" % device.name
        }


class DeviceList(Resource):
    """Device resource creation and get list of device resources
    """

    def get(self):
        schema = DeviceSchema(many=True)
        query = Device.query
        return paginate(query, schema)

    def post(self):
        schema = DeviceSchema()
        device, errors = schema.load(request.json)
        if errors:
            return errors, 422

        db.session.add(device)
        db.session.commit()

        return {
            'msg': 'Device %s created' % device.name,
            'device': schema.dump(device).data
        }, 201
