import traceback

from flask.views import MethodView
from flask import request

from database import Database

db = Database()

class GetVillage(MethodView):

    def get(self):
        try:
            args = request.args
            district = args.get('district')
            taluk = args.get('taluk')
            villages = db.get_villages(district, taluk)
            data = {
                'error' : False,
                'villages' : villages
            }
        except:
            traceback.print_exc()
            data = {
                'error' : True,
                'msg' : 'Internal Error'
            }
        return data