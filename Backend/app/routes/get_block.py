import traceback

from flask.views import MethodView
from flask import request

from database import Database

db = Database()

class GetBlock(MethodView):

    def get(self):
        try:
            args = request.args
            district = args.get('district')
            taluk = args.get('taluk')
            village = args.get('village')
            block_nos = db.get_block_nos(district, taluk, village)
            data = {
                'error' : False,
                'block_nos' : block_nos
            }
        except:
            traceback.print_exc()
            data = {
                'error' : True,
                'msg' : 'Internal Error'
            }
        return data