import traceback
import re
import os

from flask.views import MethodView
from flask import request
import cloudmersive_ocr_api_client

def process_ocr(image):
    API_KeY = "a29a390d-f62b-4d96-8dc2-2c6039bf8626"
    api_instance = cloudmersive_ocr_api_client.ImageOcrApi()

    api_instance.api_client.configuration.api_key = {}
    api_instance.api_client.configuration.api_key['Apikey'] = API_KeY

    api_response = api_instance.image_ocr_post(image)
    return str(api_response)

def extract_data(text):
    district = re.search('district.*', text.lower())
    taluk = re.search('taluk.*', text.lower())
    block_no = re.search('block.*', text.lower())
    village = re.search('village.*', text.lower())

    d = district.group().replace("\n", '').replace("'", '').split(' ')[-1]
    t = taluk.group().replace("\n", '').replace("'", '').split(' ')[-1]
    b = block_no.group().replace("\n", '').replace("'", '').split(' ')[-1]
    v = village.group().replace("\n", '').replace("'", '').split(' ')[-1]

    return d, t, b, v

class Preprocess(MethodView):

    def post(self):
        try:
            if not request.files:
                data = {
                    'error': True,
                    'msg': 'No file'
                }
            else:
                files = request.files.get('file')
                
                print(files.filename)
                filename = 'files/' + files.filename
                files.save(filename)

                ocr_txt = process_ocr(filename)
                os.remove(filename)
                district, taluk, block_no, village = extract_data(ocr_txt)
                
                data = {
                    'error': False,
                    'data': {
                        'district' : district,
                        'taluk' : taluk,
                        'block_no' : block_no,
                        'village' : village
                    }
                }
        except:
            traceback.print_exc()


            data = {
                'error': True,
                'msg': 'Internal error occoured'
            }
        return data