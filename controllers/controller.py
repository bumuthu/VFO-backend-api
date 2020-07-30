from flask_restful import Resource
from flask import request
from smplifyx import smplifyx


class Controller(Resource):

    def __init__(self):
        print('Controller got response...')

    def get(self):
        return {"message" : "Hello! I am working"}, 200

    def post(self):
        data_in = request.get_json(force=True)

        image = data_in['image']
        gender = data_in['gender']
        focal_length = data_in['focal_length']
        smplifyx_inst = smplifyx.Smplifyx(image, gender, focal_length)

        response = {
            'betas':  smplifyx_inst.get_betas(),
            }

        return response, 200