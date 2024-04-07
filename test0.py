import numpy as np
from PIL import Image
import tensorflow as tf

def preprocess_image(image_path):
    img = Image.open(image_path).convert('L')  # premeniť na čiernobiele
    img = img.resize((24, 24))  # zmeniť veľkosť
    img = np.array(img) / 255.0 
    return img

# načítať model
def load_model(model_path):
    return tf.keras.models.load_model(model_path)

def classify_image(image_path, model):
    # Preprocess the image
    img = preprocess_image(image_path)
    # Reshape the image to match the input shape of the model
    img = np.reshape(img, (1, 24, 24))
    # Predict the class probabilities
    probabilities = model.predict(img)
    # Get the predicted class label
    predicted_class = np.argmax(probabilities)
    return predicted_class, probabilities[0][predicted_class]

# obrázok na rozoznanie
new_image_path = "C:\\img.png"

# vytrénovaný model
model_path = "C:\\model.h5"

# načítať model
model = load_model(model_path)

# rozoznať obrázok
predicted_class, confidence = classify_image(new_image_path, model)

print("Trieda:", predicted_class)
print("Pismeno:", chr(65+predicted_class))
print("Istota:", confidence)

