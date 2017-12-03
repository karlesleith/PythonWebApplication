#Author : Karle Sleith
#Refrenced http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
#Refrenced https://stackoverflow.com/questions/2323128/convert-string-in-base64-to-image-and-save-on-filesystem-in-python
#Refrenced https://keras.io/getting-started/faq/
#Note that you will first need to install HDF5 and the Python library h5py, which do not come bundled with Keras

##Import packages
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import os
import sys
sys.path.append(os.path.abspath('./mnist_model'))
import keras as kr
import re, base64
import tensorflow as tf
from scipy.misc import imread, imresize, imsave,imshow
from keras.models import model_from_json
import keras.models
import codecs
import io

#initialization  of the mnist_model
def init():
    json_file = open('mnist_model.json','r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights('mnist_model.h5')
    print("LOADED MODEL 'mnist_model.h5'")

    loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    graph = tf.get_default_graph()
    return loaded_model,graph


model, graph = init()


#Define the flask
app = Flask(__name__)

#Def to covert the image from Base64
def convertImage(imgData):
    imgStr = re.search(b'base64,(.*)',imgData).group(1)
   # print("IMAGE STRING ",imgStr)
    with open('./uploads/test.png','wb') as output:
       output.write(base64.b64decode(imgStr))

#home route
@app.route("/")
def index():
    return render_template("index.html")
	
#method of the prediction
@app.route("/predict", methods=['GET','POST'])
def upload_file():
    #get raw data from the image
    imgData = request.get_data()
    #encode it into a suitable format
    convertImage(imgData)
    #inverts the image to Black and White(Greyscale)
    newImg = imread('./uploads/test.png', mode = 'L')
    #bitwise  insersion so black becomes white ect
    #newImg = np.invert(newImg)
    #make it the right size px
    newImg = imresize(newImg,(28,28))
    #covert it to a 4d tensor
    newImg = newImg.reshape(1,28,28,1)
    #computing graph preforms the prediction
    with graph.as_default():
        output = model.predict(newImg)
        print(output)
        responce = np.array_str(np.argmax(output,axis=1))
        print("THE ANSWER is: ",responce)
        return responce
#run on default
if __name__ == "__main__":
		app.run(debug=True)