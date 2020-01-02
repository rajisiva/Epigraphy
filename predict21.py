import transliterate21
from keras.models import load_model
import cv2
import numpy as np
import os



directory = "./Final_set/script2/cropped_char_test01/char"
model = load_model('21_char.hdf5')

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

total = {}
for image in os.listdir(directory):
	print(image)
	img = cv2.imread(os.path.join(directory,image))

	img = cv2.resize(img,(150,150))
	img = np.reshape(img,[1,150,150,3])

	classes = model.predict(img)

	print(classes)
	class_number = np.argmax(classes)
	print(class_number)
	# total.append(transliterate.transliterate(class_number))
	char_order = int(image.split('.')[1])
	total[char_order] = transliterate21.transliterate(class_number)
final = []
for i in range(1,len(total)+1):
	final.append(total[i])

print(" ".join(final))
