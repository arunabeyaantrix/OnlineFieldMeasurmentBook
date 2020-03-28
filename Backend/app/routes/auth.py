import hashlib

from flask.views import MethodView
from flask import request

from database import Database

db = Database()

class Auth(MethodView):

    def post(self):
        if not request.get_json():
            return {"loged_in": False}
        json_data = request.get_json()
        username = json_data.get('username')
        password = json_data.get('password')
        print(username, password)
        hash_password =  hashlib.md5(password.encode()).hexdigest()

        stored_password = db.get_user_stored_password(username)

        if hash_password == stored_password:
            return {"loged_in": True}
        
        return {"loged_in": False}