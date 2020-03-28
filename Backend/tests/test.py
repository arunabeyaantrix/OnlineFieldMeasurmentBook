import requests
import hashlib

files = {'file': open('image.jpg', 'rb')}

payload = {
    'district': 'kottatam',
    'taluk' : "meenachil",
    'block_no' : '1',
    'village' : 'meenachil',
    'survey_no' : '465'
}
file = {
    'file' : open('image.jpg', 'rb')
}

r = requests.post('http://127.0.0.1:5000/api/upload', data=payload, files = file)


print(r.text)

#print(hashlib.md5("password".encode()).hexdigest())
"""5f4dcc3b5aa765d61d8327deb882cf99"""