# PythonWebApplication
Project Assessment for Emerging Technologies 2017 

![alt text](https://github.com/karlesleith/PythonWebApplication/blob/master/static/ReadmeImg.PNG)


## Overview
In this project I will create a web application in Python using Flask to recognise digits in images. Users will be able to visit the web application through their browser,and draw an image containing a single digit [1-10], and the web application will respond with the digit contained in the image. The application uses "Keras" with a Tensorflow backend. The application runs with an accuracy of 99% when reconising digits. This web application will be used as an "Emerging Technologies" Project, due December 4th 2017.

## Project Instructions
1. Create a git repository with a README.md and an appropriate gitignore file. The README should explain who you are, why you created the application, how you created it, how to download and run it, and summarise any references you have used.
2. In the repository, create a web application that serves a HTML page as the root resource. The page should contain an input where the user can upload (or draw) an image containing a digit, and an area to display the image and the digit.
3. Add a route to your application that accepts requests containing a user input image and responds with the digit.
Connect the HTML page to the route using AJAX.

## What is the MNIST Data Set?
The MNIST database (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems. The database is also widely used for training and testing in the field of machine learning. It was created by "re-mixing" the samples from NIST's original datasets. The creators felt that since NIST's training dataset was taken from American Census Bureau employees, while the testing dataset was taken from American high school students, it was not well-suited for machine learning experiments. Furthermore, the black and white images from NIST were normalized to fit into a 28x28 pixel bounding box and anti-aliased, which introduced grayscale levels..


**REF**: [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)

http://yann.lecun.com/exdb/mnist/

## What is Tensorflow?
TensorFlow is an open source software library for numerical computation using data flow graphs. Nodes in the graph represent mathematical operations, while the graph edges represent the multidimensional data arrays (tensors) communicated between them. The flexible architecture allows you to deploy computation to one or more CPUs or GPUs in a desktop, server, or mobile device with a single API. 

**REF**: [https://www.tensorflow.org/](https://www.tensorflow.org/)

## What is Keras?
Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano. It was developed with a focus on enabling fast experimentation. Being able to go from idea to result with the least possible delay is key to doing good research.

**REF**: [https://keras.io/](https://keras.io/)

## How to run the Web Application 

Make sure you have at least Python 3.5 installed

**REF** [https://www.python.org/downloads/](https://www.python.org/downloads/)

Be sure install Keras, Flask HD5F and h5py and upgraded to latest version

`pip --upgrade keras`
`pip --upgrade scipy`
`pip --upgrade HD5F`
`pip --upgrade h5py`
`pip --upgrade flask`

Clone the repo to your desktop, navigate to the directory of the repo, and in the command prompt type

`python app.py`

This will launch the Flask Application on  http://127.0.0.1:5000/

# How to re-train the model 

Clone the repo to your desktop, navigate to the directory of the repo, and in the command prompt type

`mnist.py`

This will re-train the model, and re-populate 'mnist_model.json' and 'mnist_model.h5', or create them if they dont exist. This process may take some time, so only do it if you want to see how the model is formed.

