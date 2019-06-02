from flask import Flask
import requests
import sys
import json
from flask import jsonify
import io
from flask import request,redirect,url_for,session,flash
app = Flask(__name__)
app.secret_key = "super secret key"
import downloader as extract
import extraction as cleanstore

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

def getjson(o):
    with open(o,'r') as json_file:
        print(json_file)
        data = json.loads(json_file)
        print(data)
        return data

@app.route('/',methods = ['POST', 'GET'])
def hel():
    if request.method == 'GET':
        youtubeid = request.args.get('youtubeid')
        youtubeid = str(youtubeid)
        print(type(youtubeid))
        print(youtubeid)

        

       
       
        try:
            limita = request.args.get('limit')      
            if(limita!=None):
                limita= int(limita)
                print(type(limita))
                out = extract.main2(youtubeid,limita)
                data=cleanstore.extractclean(out)
               
            else:
                out= extract.main2(youtubeid)
                data=cleanstore.extractclean(out)
        except Exception as e:
            print('Error:', str(e))
        print(out)
        
        
        

        return jsonify(data)



       
        
       
       



    
       

        




        
        





if __name__ == '__main__':
    app.run(port=5200,debug=True)