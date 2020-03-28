import traceback

from flask.views import MethodView
from flask import request

from database import Database

db = Database()

class GetTaluk(MethodView):

    def get(self):
        try:
            args = request.args
            district = args.get('district')
            taluks = db.get_taluks(district)
            data = {
                'error' : False,
                'taluks' : taluks
            }
        except:
            traceback.print_exc()
            data = {
                'error' : True,
                'msg' : 'Internal Error'
            }
        return data