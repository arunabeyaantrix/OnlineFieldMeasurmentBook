import traceback

from flask.views import MethodView
from flask import request

from database import Database

db = Database()

class GetSurvey(MethodView):

    def get(self):
        try:
            args = request.args
            district = args.get('district')
            taluk = args.get('taluk')
            village = args.get('village')
            block_no = int(args.get('block_no'))
            survey_nos = db.get_survey_nos(district, taluk, village, block_no)
            data = {
                'error' : False,
                'survey_nos' : survey_nos
            }
        except:
            traceback.print_exc()
            data = {
                'error' : True,
                'msg' : 'Internal Error'
            }
        return data