
import sys
sys.path.append('image-super-resolution')

import fire
from PIL import Image
from pathlib import Path
import numpy as np
from flask import Flask, request, jsonify

from ISR.models import RDN, RRDN

def get_info_request(request):
    print(request)
    #data = request.json()
    #print(data)
    return request.json['input'],request.json['output']

if __name__=="__main__":

    endpoint_name = 'srapi'
    port = 5050
    host = '0.0.0.0'

    model = RDN(weights='noise-cancel')

    app = Flask(__name__)
    @app.route(f'/{endpoint_name}', methods=['POST','GET'])
    def predict():

        if request.method == 'POST':

            input, output = get_info_request(request)

            img = Image.open(input)
            sr_img = model.predict(np.array(img))
            sr_img = Image.fromarray(sr_img)
            sr_img.save(output)

            #status_code = flask.Response(status=201)
            #return status_code
            return jsonify({'message':'successful'})


        if request.method == 'GET':
            message = "I am a model for enhancing low-resolution images"
            return jsonify({'greetings':message})


    app.run(host=host, port=port)
