import traceback
import base64
import os

from flask.views import MethodView
from flask import request
import requests

from database import Database

db = Database()

def insert_item(district, taluk, village, block_no, survey_no, image):
    districts = db.get_districts()
    if district.lower() not in districts:
        db.create_district(district)

    taluks = db.get_taluks(district)

    if taluk not in taluks:
        db.create_taluk(district, taluk)
    
    villages = db.get_villages(district, taluk)

    if village not in villages:
        db.create_village(district, taluk, village)
    
    block_nos = db.get_block_nos(district, taluk, village)

    if block_no not in block_nos:
        db.create_block_no(district, taluk, village, block_no)
    
    survey_nos = db.get_survey_nos(district, taluk, village, block_no)

    if survey_no not in survey_nos:
        db.create_survey_no(district, taluk, village, block_no, survey_no)
    
    file_url = save_file(image)

    db.save_image(district, taluk, village, block_no, survey_no, file_url)

def save_file(image):
    with open(image, 'rb') as img_file:
        my_string = base64.b64encode(img_file.read())

    r = requests.post('https://api.imgbb.com/1/upload',
        params = {
            'key': 'e3eca0be62cf52b527bc5799af1df52b'
        },
        data = {
            'image': my_string
        }
    )

    resp = r.json()
    os.remove(image)

    return resp['data']['url']



class Upload(MethodView):

    def post(self):
        try:
            if not request.form:
                return {'error': True, 'msg': "not a form"}
            if not request.files:
                return {'error': True, 'msg': "no file attached"}
            form_data = request.form
            files = request.files.get('file')
            filename = 'files/' + files.filename
            files.save(filename)
            
            district = form_data.get('district')
            taluk = form_data.get('taluk')
            block_no = int(form_data.get('block_no'))
            village = form_data.get('village')
            survey_no = int(form_data.get('survey_no'))

            insert_item(district, taluk, village, block_no, survey_no, filename)

            return {'error': False}
        except:
            traceback.print_exc()
            return {'error': True, 'msg': "Internal Error"}