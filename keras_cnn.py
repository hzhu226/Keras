import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow import keras
from tensorflow.keras.layers import Flatten, Dense, Conv2D
import numpy as np

def get_dataset(training=True):
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
    i = np.array(train_images)
    i.shape
    x = np.expand_dims(i, axis=3)
    x.shape
    j = np.array(test_images)
    j.shape
    y = np.expand_dims(j, axis=3)
    y.shape
    if training:
        return (x, train_labels)
    else:
        return (y, test_labels)

def build_model():
    model = keras.Sequential()
    model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28, 28, 1)))
    model.add(Conv2D(32, kernel_size=3, activation='relu'))
    model.add(Flatten())
    model.add(Dense(10, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def train_model(model, train_img, train_lab, test_img, test_lab, T):
    train_lab = keras.utils.to_categorical(train_lab)
    test_lab = keras.utils.to_categorical(test_lab)
    model.fit(train_img, train_lab, validation_data=(test_img, test_lab), epochs=T)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def predict_label(model, images, index):
    predict = model.predict(images)
    class_labels = []
    for i in range(len(predict[index])):
        class_labels.append((predict[index][i], class_names[i]))
    class_labels = sorted(class_labels, key=lambda class_labels: class_labels[0], reverse=True)
    for j in range(3):
        print('{}: {:.2f}%'.format(class_labels[j][1], class_labels[j][0] * 100))
