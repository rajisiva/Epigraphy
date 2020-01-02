from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import matplotlib.pyplot as plt


# dimensions of our images.
img_width, img_height = 150, 150

train_data_dir = '../Data/21_char'
nb_train_samples = 2129

epochs = 200
batch_size = 16

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(21))
model.add(Activation('softmax'))
model.summary()
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)


train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')


history = model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs)

with open("accuracy.txt","w") as f:
	for i in range(0,len(history.history['acc'])):
		f.write(str(history.history['acc'][i]))
		f.write("\n")
f.close()
with open("loss.txt","w") as f:
	for i in range(0,len(history.history['acc'])):
		f.write(str(history.history['loss'][i]))
		f.write("\n")
f.close()

plt.figure(1)
plt.title('training accuracy')
plt.plot(history.history['acc'])
plt.xlabel('epoch')
plt.ylabel('accuracy')

plt.savefig('accuracy.png')
plt.figure(2)
plt.title('training loss')
plt.plot(history.history['loss'])
plt.xlabel('epoch')
plt.ylabel('loss')

plt.savefig('loss.png')
model.save('21_char.hdf5')
model.save_weights('21_char.h5')
model_json = model.to_json()
with open("21_char.json","w") as f:
    f.write(model_json)
