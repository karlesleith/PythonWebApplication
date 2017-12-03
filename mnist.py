# Karle Sleith G00324919	
# Refrences
# https://github.com/yashk2810/MNIST-Keras/blob/master/Notebook/MNIST_keras_CNN-99.55%25.ipynb
# https://keras.io/getting-started/sequential-model-guide/

#Import librarys
import numpy as np
from keras.datasets import mnist
import keras as kr
from keras.layers.advanced_activations import LeakyReLU
from keras.preprocessing.image import ImageDataGenerator


# Loading the MNIST Dataset
(x_train,y_train),(x_test,y_test) = mnist.load_data()

print("X_train original shape", x_train.shape)
print("y_train original shape", y_train.shape)
print("X_test original shape", x_test.shape)
print("y_test original shape", y_test.shape)

#Reshaping the Train and Test
x_train = x_train.reshape(x_train.shape[0],28,28,1)
x_test = x_test.reshape(x_test.shape[0],28,28,1)

#setting the types to float32
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

#used for testing 
print("let's see where we are :",x_train.shape)

number_of_classes = 10;

#encode to binary
y_train = kr.utils.np_utils.to_categorical(y_train,number_of_classes)
y_test = kr.utils.np_utils.to_categorical(y_test,number_of_classes)

#divide to get a 0 or 1
x_train = x_train/255
x_test = x_test/255

#creates the neural network
model = kr.models.Sequential()

#adding the convolution 2D layer
model.add(kr.layers.Conv2D(32,(3,3),input_shape=(28,28,1)))
kr.layers.normalization.BatchNormalization(axis=-1)
#adding the relu activation function, A smooth approximation to the rectifier is the analytic function.
model.add(kr.layers.Activation('relu'))
model.add(kr.layers.Conv2D(32,(3,3)))
kr.layers.normalization.BatchNormalization(axis=-1)
model.add(kr.layers.Activation('relu'))
model.add(kr.layers.MaxPooling2D(pool_size=(2,2)))

model.add(kr.layers.Conv2D(64,(3,3)))
kr.layers.normalization.BatchNormalization(axis=-1)
model.add(kr.layers.Activation('relu'))
model.add(kr.layers.Conv2D(64,(3,3)))
kr.layers.normalization.BatchNormalization(axis=-1)
model.add(kr.layers.Activation('relu'))
model.add(kr.layers.MaxPooling2D(pool_size=(2,2)))

model.add(kr.layers.Flatten())
model.add(kr.layers.Dense(512))
kr.layers.normalization.BatchNormalization()
model.add(kr.layers.Activation('relu'))
model.add(kr.layers.Dropout(0.2))
model.add(kr.layers.Dense(10))

#softmax "squishes" everything together
model.add(kr.layers.Activation('softmax'))

# Configure the model for training.
# Uses the adam optimizer and categorical cross entropy as the loss function.
# Add in some extra metrics - accuracy being the only one.
model.compile(loss='categorical_crossentropy',optimizer= kr.optimizers.Adam(), metrics =['accuracy'] )

# Fit the model using our training data.
gen = ImageDataGenerator(rotation_range= 8 , width_shift_range=0.08,shear_range=0.3,height_shift_range=0.08,zoom_range=0.08)
test_gen = ImageDataGenerator()

train_gen = gen.flow(x_train,y_train,batch_size=64)
test_generator = gen.flow(x_test,y_test,batch_size=64)

model.fit_generator(train_gen,steps_per_epoch=60000//64, epochs=5, validation_data = test_generator, validation_steps = 10000//64)

#We'll print the accuracy to the screen
acc = (x_test,y_test)
print()
print('Accuracy', acc[1])

#Save the model for both the .h5(so we can load it again later), and the json that we can pass to App.py
model_json = model.to_json()
with open("mnist_model.json",'w') as json_file:
    json_file.write(model_json)

## Save the model to a file for later use.
model.save_weights("mnist_model.h5")
# Load the model again with: model = load_model("mnist_model.h5")