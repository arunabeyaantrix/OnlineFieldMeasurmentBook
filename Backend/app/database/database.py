import pymongo

client = pymongo.MongoClient("mongodb+srv://root:root@cluster0-cg3ab.mongodb.net/test?retryWrites=true&w=majority")

class Database:
    def __init__(self):
        self.admin_db = client["admins"]['admins']
        self.doc_db = client["documents"]
        self.district_col = self.doc_db['districts']
        self.taluk_col = self.doc_db['taluks']
        self.village_col = self.doc_db['villages']
        self.block_col = self.doc_db['blocks']
        self.survey_col = self.doc_db['surveys']
        self.image_col = self.doc_db['images']
    
    def get_user_stored_password(self, username):
        data = self.admin_db.find_one(
            {
                'username' : username
            }
        )
        if not data:
            return ''   
        return data.get('password', '')
    
    def get_districts(self):
        districts = self.district_col.find()
        return [i['name'].lower() for i in districts]
    
    def create_district(self, district):
        self.district_col.insert_one(
            {
                'name' : district
            }
        )
    
    def get_taluks(self, district):
        taluks = self.taluk_col.find({
            'district' : district
        })
        return [i['name'].lower() for i in taluks]
    
    def create_taluk(self, district, taluk):
        self.taluk_col.insert_one(
            {
                'name' : taluk,
                'district' : district
            }
        )
    
    def get_villages(self, district, taluk):
        villages = self.village_col.find({
            'district' : district,
            'taluk' : taluk
        })
        return [i['name'].lower() for i in villages]
    
    def create_village(self, district, taluk, village):
        self.village_col.insert_one(
            {
                'name' : village,
                'district' : district,
                'taluk' : taluk
            }
        )
    
    def get_block_nos(self, district, taluk, village):
        blocks = self.block_col.find({
            'district' : district,
            'taluk' : taluk,
            'village' : village
        })
        return [i['no'] for i in blocks]
    
    def create_block_no(self, district, taluk, village, block_no):
        self.block_col.insert_one(
            {
                'no' : block_no,
                'village' : village,
                'district' : district,
                'taluk' : taluk
            }
        )
    
    def get_survey_nos(self, district, taluk, village, block_no):
        surveys = self.survey_col.find({
            'district' : district,
            'taluk' : taluk,
            'village' : village,
            'block_no' : block_no
        })
        return [i['no'] for i in surveys]
    
    def create_survey_no(self, district, taluk, village, block_no, survey_no):
        self.survey_col.insert_one(
            {
                'block_no' : block_no,
                'village' : village,
                'district' : district,
                'taluk' : taluk,
                'no' : survey_no
            }
        )
    
    def save_image(self, district, taluk, village, block_no, survey_no, file_url):
        self.image_col.insert_one(
            {
                'block_no' : block_no,
                'village' : village,
                'district' : district,
                'taluk' : taluk,
                'survey_no' : survey_no,
                'url'  : file_url
            }
        )
    
    def get_image(self, district, taluk, village, block_no, survey_no):
        image = self.image_col.find({
            'district' : district,
            'taluk' : taluk,
            'village' : village,
            'block_no' : block_no,
            'survey_no' : survey_no
        })
        print(image)
        return [i['url'] for i in image]