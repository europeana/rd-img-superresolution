from PIL import Image
from pathlib import Path
import numpy as np
from flask import Flask, request, jsonify

import sys
sys.path.append('image-super-resolution')
from ISR.models import RDN, RRDN

if __name__=="__main__":

    endpoint_name = 'srapi'
    port = 5050
    host = '0.0.0.0'

    model = RDN(weights='noise-cancel')

    app = Flask(__name__)
    @app.route(f'/{endpoint_name}', methods=['POST','GET'])
    def predict():

        if request.method == 'POST':
            img = Image.open(request.json['input'])
            sr_img = model.predict(np.array(img))
            sr_img = Image.fromarray(sr_img)
            sr_img.save(request.json['output'])
            return jsonify({'message':'successful'})

        if request.method == 'GET':
            return jsonify({'message':"I am a model for enhancing low-resolution images"})

    app.run(host=host, port=port)
