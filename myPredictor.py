import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model

img_width, img_height = 150, 150
model_path = './models/model.h5'
model_weights_path = './models/weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)

def predict(file):
  x = load_img(file, target_size=(img_width,img_height))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  x = np.array(x)
  array = model.predict(x)
  result = array[0]
  answer = np.argmax(result)
  if answer == 0:
    print("Label: Arali")
  elif answer == 1:
    print("Label: Arasamaram")
  elif answer == 2:
    print("Label: Ashoka")
  elif answer == 3:
    print("Label: Beetle")
  elif answer == 4:
    print("Label: Curryleaf")
  elif answer == 5:
    print("Label: Erukkampoo")
  elif answer == 6:
    print("Label: Hibiscus")
  elif answer == 7:
    print("Label: JackFruit")
  elif answer == 8:
    print("Label: Lemon")
  elif answer == 9:
    print("Label: Mango")
  elif answer == 10:
    print("Label: Murungai")
  elif answer == 11:
    print("Label: Nagalingapoo")
  elif answer == 12:
    print("Label: Neem")
  elif answer == 13:
    print("Label: Pudhina")
  return answer


Arali_t = 0
Arali_f = 0
Arasamaram_t = 0
Arasamaram_f = 0
Ashoka_t = 0
Ashoka_f = 0
Beetle_t = 0
Beetle_f = 0
Curryleaf_t = 0
Curryleaf_f = 0
Erukkampoo_t = 0
Erukkampoo_f = 0
Hibiscus_t = 0
Hibiscus_f = 0
JackFruit_t = 0
JackFruit_f = 0
Lemon_t = 0
Lemon_f = 0
Mango_t = 0
Mango_f = 0
Murungai_t = 0
Murungai_f = 0
Nagalingapoo_t = 0
Nagalingapoo_f = 0
Neem_t = 0
Neem_f = 0
Pudhina_t = 0
Pudhina_f = 0

for i, ret in enumerate(os.walk('./test-data/Arali')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Actual Label: Arali")
    result = predict(ret[0] + '/' + filename)
    if result == 0:
      Arali_t += 1
    else:
      Arali_f += 1


for i, ret in enumerate(os.walk('./test-data/Arasamaram')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Actual Label: Arasamaram")
    result = predict(ret[0] + '/' + filename)
    if result == 1:
      Arasamaram_t += 1
    else:
      Arasamaram_f += 1

for i, ret in enumerate(os.walk('./test-data/Ashoka')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Actual Label: Ashoka")
    result = predict(ret[0] + '/' + filename)
    if result == 2:
      Ashoka_t += 1
    else:
      Ashoka_f += 1

for i, ret in enumerate(os.walk('./test-data/Beetle')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Actual Label: Beetle")
    result = predict(ret[0] + '/' + filename)
    if result == 3:
      Beetle_t += 1
    else:
      Beetle_f += 1


for i, ret in enumerate(os.walk('./test-data/Curryleaf')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Actual Label: Curryleaf")
    result = predict(ret[0] + '/' + filename)
    if result == 4:
      Curryleaf_t += 1
    else:
      Curryleaf_f += 1

for i, ret in enumerate(os.walk('./test-data/Erukkampoo')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Actual Label: Erukkampoo")
    result = predict(ret[0] + '/' + filename)
    if result == 5:
      Erukkampoo_t += 1
    else:
      Erukkampoo_f += 1


for i, ret in enumerate(os.walk('./test-data/Hibiscus')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Actual Label: Hibiscus")
    result = predict(ret[0] + '/' + filename)
    if result == 6:
      Hibiscus_t += 1
    else:
      Hibiscus_f += 1


for i, ret in enumerate(os.walk('./test-data/JackFruit')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Actual Label: JackFruit")
    result = predict(ret[0] + '/' + filename)
    if result == 7:
      JackFruit_t += 1
    else:
      JackFruit_f += 1


for i, ret in enumerate(os.walk('./test-data/Lemon')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Actual Label: Lemon")
    result = predict(ret[0] + '/' + filename)
    if result == 8:
      Lemon_t += 1
    else:
      Lemon_f += 1


for i, ret in enumerate(os.walk('./test-data/Mango')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Actual Label: Mango")
    result = predict(ret[0] + '/' + filename)
    if result == 9:
      Mango_t += 1
    else:
      Mango_f += 1


for i, ret in enumerate(os.walk('./test-data/Murungai')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Actual Label: Murungai")
    result = predict(ret[0] + '/' + filename)
    if result == 10:
      Murungai_t += 1
    else:
      Murungai_f += 1


for i, ret in enumerate(os.walk('./test-data/Nagalingapoo')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Actual Label: Nagalingapoo")
    result = predict(ret[0] + '/' + filename)
    if result == 11:
      Nagalingapoo_t += 1
    else:
      Nagalingapoo_f += 1


for i, ret in enumerate(os.walk('./test-data/Neem')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Actual Label: Neem")
    result = predict(ret[0] + '/' + filename)
    if result == 12:
      Neem_t += 1
    else:
      Neem_f += 1


for i, ret in enumerate(os.walk('./test-data/Pudhina')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Actual Label: Pudhina")
    result = predict(ret[0] + '/' + filename)
    if result == 13:
      Pudhina_t += 1
    else:
      Pudhina_f += 1


"""
Check metrics
"""
print("True Arali: ", Arali_t)
print("False Arali: ", Arali_f)
print("True Arasamaram: ", Arasamaram_t)
print("False Arasamaram: ", Arasamaram_f)
print("True Ashoka: ", Ashoka_t)
print("False Ashoka: ", Ashoka_f)
print("True Beetle: ", Beetle_t)
print("False Beetle: ", Beetle_f)
print("True Curryleaf: ", Curryleaf_t)
print("False Curryleaf: ", Curryleaf_f)
print("True Erukkampoo: ", Erukkampoo_t)
print("False Erukkampoo: ", Erukkampoo_f)
print("True Hibiscus: ", Hibiscus_t)
print("False Hibiscus: ", Hibiscus_f)
print("True JackFruit: ", JackFruit_t)
print("False JackFruit: ", JackFruit_f)
print("True Lemon: ", Lemon_t)
print("False Lemon: ", Lemon_f)
print("True Mango: ", Mango_t)
print("False Mango: ", Mango_f)
print("True Murungai: ", Murungai_t)
print("False Murungai: ", Murungai_f)
print("True Nagalingapoo: ", Nagalingapoo_t)
print("False Nagalingapoo: ", Nagalingapoo_f)
print("True Neem: ", Neem_t)
print("False Neem: ", Neem_f)
print("True Pudhina: ", Pudhina_t)
print("False Pudhina: ", Pudhina_f)
