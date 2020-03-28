from flask import Flask
from flask_cors import CORS

from routes import Preprocess, Upload, Auth, GetDistricts, GetTaluk, GetVillage, GetBlock, GetSurvey, GetImage, Home

app = Flask(__name__)
CORS(app)

def setup_app(app):
    app.add_url_rule('/api/preprocess', view_func=Preprocess.as_view('preprocess'))
    app.add_url_rule('/api/upload', view_func=Upload.as_view('upload'))
    app.add_url_rule('/api/login', view_func=Auth.as_view('login'))
    app.add_url_rule('/api/districts', view_func=GetDistricts.as_view('districts'))
    app.add_url_rule('/api/taluks', view_func=GetTaluk.as_view('taluks'))
    app.add_url_rule('/api/villages', view_func=GetVillage.as_view('villages'))
    app.add_url_rule('/api/blocks', view_func=GetBlock.as_view('blocks'))
    app.add_url_rule('/api/surveys', view_func=GetSurvey.as_view('survey'))
    app.add_url_rule('/api/image', view_func=GetImage.as_view('image'))
    app.add_url_rule('/', view_func=Home.as_view('home'))

if __name__ == '__main__':
    setup_app(app)
    app.run(host='0.0.0.0')