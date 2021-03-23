from tensorflow import keras
from tensorflow.keras.layers import Flatten, Dense, Activation, Softmax
from tensorflow.keras.losses import SparseCategoricalCrossentropy
import matplotlib.pyplot as mat

def get_dataset(training=True):
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
    if training:
        return (train_images, train_labels)
    else:
        return (test_images, test_labels)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def print_stats(images, labels):
    num = [0] * 10
    for i in labels:
        num[i] = num[i] + 1
    print(len(images))
    str_0 = '{}x{}'
    print(str_0.format(len(images[0]), len(images[0][0])))
    for j in range(len(class_names)):
        str_1 = '{}. {} - {}'
        print(str_1.format(j, class_names[j], num[j]))

def view_image(image, label):
    ob, ax = mat.subplots()
    ax.set_title(label)
    image = ax.imshow(image, aspect='equal')
    ob.colorbar(image, ax=ax)
    mat.show()

def build_model():
    model = keras.Sequential()
    model.add(Flatten(input_shape=(28, 28)))
    model.add(Dense(128, activation=Activation('relu')))
    model.add(Dense(10))

    model.compile(loss=SparseCategoricalCrossentropy(from_logits=True), optimizer='adam', metrics=['accuracy'])
    return model

def train_model(model, images, labels, T):
    model.fit(x=images, y=labels, epochs=T)

def evaluate_model(model, images, labels, show_loss=True, verbose=0):
    test_loss, test_accuracy = model.evaluate(images, labels)
    if show_loss == True:
        print('Loss: {:.2f}'.format(test_loss))
    print('Accuracy: {:.2f}%'.format(test_accuracy * 100))

def predict_label(model, images, index):
    model.add(Softmax())
    predict = model.predict(images)
    class_labels = []
    for i in range(len(predict[index])):
        class_labels.append((predict[index][i], class_names[i]))
    class_labels = sorted(class_labels, key=lambda class_labels: class_labels[0], reverse=True)
    for j in range(3):
        print('{}: {:.2f}%'.format(class_labels[j][1], class_labels[j][0] * 100))