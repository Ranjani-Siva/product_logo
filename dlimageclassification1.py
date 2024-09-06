# -*- coding: utf-8 -*-
"""DLimageClassification1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u3YyBrXfPD5snHTVgRdld1g34FriQcDh

Problem Statement: Classify the Food Product Indian Company Logo of 25 Company's.
Dataset: Synthetic dataset from Various offical website of the company and from google images and pinterest website.
Using tensorflow develop the sequence model with CNN and test the model with test data.
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

PATH = '/content/drive/MyDrive/Colab Notebooks'
train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'validation')
test_dir = os.path.join(PATH, 'test')
print(train_dir)
print(validation_dir)
print(test_dir)

train_dataset = image_dataset_from_directory(
 train_dir,
 image_size=(180, 180),
 batch_size=32)

validation_dataset = image_dataset_from_directory(
 validation_dir,
 image_size=(180, 180),
 batch_size=32)

test_dataset = image_dataset_from_directory(
 test_dir,
 image_size=(180, 180),
 batch_size=32)

class_names = ["7up","Amul","Balaji Wafers","Bingo","Britannia","Cheetos","Coco Cola","Dabur","Fanta","Haldiram's","Hershey's",
               "Kellogg's","Kissan","Kurkure","Lays","Maaza","Maggi","Mc Cain","Mother Dairy","Mtr","Orea","Paper boat",
               "Roof afza","Sunfeast","Vadilal"]

plt.figure(figsize=(10,10))
# Iterate over the dataset and take only the first 25 images and labels
for images, labels in train_dataset.take(25):
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        # Display the image
        plt.imshow(images[i].numpy().astype("uint8"))
        # Display the label
        plt.xlabel(class_names[labels[i]])
plt.show()

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(180, 180, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(25))

model.summary()

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_dataset, epochs=10,
                    validation_data=validation_dataset)

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

test_loss, test_acc = model.evaluate(test_dataset, verbose=2)

"""# To improve the model data augmentation take place in next colab link:
https://colab.research.google.com/drive/11BSssi7O0MaCtoRfL3lB951ba_zhOvH0?usp=sharing
"""