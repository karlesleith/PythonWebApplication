#Author : Karle Sleith
#Refrenced http://flask.pocoo.org/docs/0.12/patterns/fileuploads/

from flask import Flask, render_template, request, redirect, url_for
import os
import keras as kr


app = Flask(__name__)

APP_ROOT_DIR = os.path.dirname(os.path.abspath("__file__"))
print(APP_ROOT_DIR)


#Using our trained Model
model = kr.models.load_model("mnist_model.h5")

@app.route("/")
def index():
    return render_template("index.html")
	

@app.route("/upload", methods=['POST'])
def upload_file():
	target = os.path.join(APP_ROOT_DIR, "uploads/")
	print(target)
	
	for file in request.files.getlist("file"):
		print(file)
		filename = file.filename
		destination ="/".join({target,filename})
		print(destination)
		file.save(destination)
		
		return str("File Uploaded")
	
if __name__ == "__main__":
	app.run(debug=True)