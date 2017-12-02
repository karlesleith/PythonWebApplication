# Karle Sleith G00324919	
# Refrences
# https://github.com/salmanahmad4u/keras-iris/blob/master/iris_nn.py
#https://github.com/yashk2810/MNIST-Keras/blob/master/Notebook/MNIST_keras_CNN-99.55%25.ipynb
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

x_train = x_train.reshape(x_train.shape[0],28,28,1)
x_test = x_test.reshape(x_test.shape[0],28,28,1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

print("let's see where we are :",x_train.shape)

number_of_classes = 10;

y_train = kr.utils.np_utils.to_categorical(y_train,number_of_classes)
y_test = kr.utils.np_utils.to_categorical(y_test,number_of_classes)

x_train = x_train/255
x_test = x_test/255

model = kr.models.Sequential()

model.add(kr.layers.Conv2D(32,(3,3),input_shape=(28,28,1)))
kr.layers.normalization.BatchNormalization(axis=-1)
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

model.add(kr.layers.Activation('softmax'))

model.compile(loss='categorical_crossentropy',optimizer= kr.optimizers.Adam(), metrics =['accuracy'] )

gen = ImageDataGenerator(rotation_range= 8 , width_shift_range=0.08,shear_range=0.3,height_shift_range=0.08,zoom_range=0.08)
test_gen = ImageDataGenerator()

train_gen = gen.flow(x_train,y_train,batch_size=64)
test_generator = gen.flow(x_test,y_test,batch_size=64)

model.fit_generator(train_gen,steps_per_epoch=60000//64, epochs=5, validation_data = test_generator, validation_steps = 10000//64)

acc = (x_test,y_test)
print()
print('Accuracy', acc[1])

## Save the model to a file for later use.
model.save("mnist_model.h5")
# Load the model again with: model = load_model("mnist_model.h5")