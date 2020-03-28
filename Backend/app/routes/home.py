from flask.views import MethodView
from flask import request

class Home(MethodView):

    def get(self):
        return {
            'hello' : 'world'
        }