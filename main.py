from flask import Flask
from flask_restful import Resource, Api
import logging as logger
from controllers import controller
from smplifyx import *
logger.basicConfig(level="DEBUG")


app = Flask(__name__)
api = Api(app)
api.add_resource(controller.Controller, '/')

if __name__ == '__main__':
    app.run(host="34.71.158.225", port=8080, debug=True, use_reloader=True)

