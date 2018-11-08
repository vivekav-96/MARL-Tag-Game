from PIL import Image
from keras import Sequential
from keras.layers import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Dense, Flatten
from keras.preprocessing.image import img_to_array

if __name__ == '__main__':
    img = Image.open("2_0.png")
    img = img.resize((96, 96))
    arr = img_to_array(img)
    img.save("2_0-resized.png")
    print(arr.shape)

    model = Sequential()
    model.add(Conv2D(32, (3, 3), padding="same", input_shape=(96, 96, 3)))
    model.add(MaxPooling2D(pool_size=(3, 3)))
    model.add(Flatten())
    model.add(Dense(8))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()

    arr = arr.reshape((1,) + arr.shape)
    print(model.predict(arr))
