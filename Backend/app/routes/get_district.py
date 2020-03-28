import traceback

from flask.views import MethodView
from flask import request

from database import Database

db = Database()

class GetDistricts(MethodView):

    def get(self):
        try:
            districts = db.get_districts()
            data = {
                'error' : False,
                'districts' : districts
            }
        except:
            traceback.print_exc()
            data = {
                'error' : True,
                'msg' : 'Internal Error'
            }
        return data