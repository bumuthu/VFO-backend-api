from flask_restful import Resource
from flask import request
from smplifyx import smplifyx


class Controller(Resource):

    def __init__(self):
        print('Controller initiated')

    def get(self):
        return {"message" : "Hello! I am working"}, 200

    def post(self):
        data_in = request.get_json(force=True)
        print(data_in)
        image = data_in['image']
        gender = data_in['gender']
        print('h1')
        smplifyx_inst = smplifyx.Smplifyx(image, gender)
        print('h2')
        response = {
            'betas':  smplifyx_inst.get_betas(),
            'texture' :  smplifyx_inst.get_texture(),
            'recommendation': smplifyx_inst.get_recommendation()
            }

        return response, 200