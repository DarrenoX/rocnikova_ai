import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models

# načítanie dát
def load_data(directory):
    data = []
    labels = []
    for label, letter in enumerate(os.listdir(directory)):
        for file in os.listdir(os.path.join(directory, letter)):
            img_path = os.path.join(directory, letter, file)
            img = Image.open(img_path).convert('L')  # premeniť na čiernobiele
            img = img.resize((24, 24))  # zmeniť veľkosť na 24x24
            img = np.array(img) / 255.0 
            data.append(img)
            labels.append(label)
    return np.array(data), np.array(labels)

directory = "C:\\dataset"
data, labels = load_data(directory)

# rozdelenie dát na trénovacie a validačné
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# neuróny
model = models.Sequential([
    layers.Flatten(input_shape=(24,24)),    # vstupná
    layers.Dense(256, activation='relu'),   # skrytá 1
    layers.Dense(128, activation='relu'),   # skrytá 2
    layers.Dense(64, activation='relu'),    # skrytá 3
    layers.Dense(26, activation='softmax')  # výstupná
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# trénovanie
model.fit(X_train, y_train, epochs=30, batch_size=128, validation_data=(X_test, y_test))

# ohodnotenie
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Test Accuracy:", test_acc)

# uloženie modelu, aby sa dal použiť
model.save("C:\\Users\\Danielko2\\models\\test0.h5")
