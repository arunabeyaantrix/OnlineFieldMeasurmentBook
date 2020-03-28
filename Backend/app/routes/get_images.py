import traceback

from flask.views import MethodView
from flask import request

from database import Database

db = Database()

class GetImage(MethodView):

    def get(self):
        try:
            args = request.args
            district = args.get('district')
            taluk = args.get('taluk')
            village = args.get('village')
            block_no = int(args.get('block_no'))
            survey_no = int(args.get('survey_no'))
            url = db.get_image(district, taluk, village, block_no, survey_no)
            print(url)
            data = {
                'error' : False,
                'url' : url
            }
        except:
            traceback.print_exc()
            data = {
                'error' : True,
                'msg' : 'Internal Error'
            }
        return data