from tensorflow.keras.models import load_model
from keras.preprocessing import image
model= load_model("gesture.h5")

import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
model = load_model("gesture.h5")
path= r'/content/drive/MyDrive/test/0/0.jpg'

img = image.load_img(path,color_mode="grayscale",target_size=(64,64))
x = image.img_to_array(img)#image to array
x = np.expand_dims (x,axis = 0) #changing the shape
pred = np.argmax(model.predict(x), axis=-1) #predicting the classes
p.append(pred)
print(p)

result = []
index = ['0', '1', '2', '3', '4', '5']
for i in p:
result.append(index[i[0]])

print(result)