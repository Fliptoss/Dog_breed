#import libraries 
import numpy as np
import streamlit as st
import cv2
from tensorflow.keras.models import load_model

#loading the model
model = load_model('dog_breed.h5')

#defining class 
CLASS_NAMES = ['Scottish Deerhound', 'Maltese Dog', 'Bernese Mountain Dog']

#setting title of app
st.title("Dog Breed Prediction")
st.markdown("Upload an image of the dog")

#uploading the image of the dog
dog_image = st.file_uploader("Choose an image of a dog.", type=["png", "jpg", "jpeg"])
submit = st.button('Predict')

#on click
if submit:
    if dog_image is not None:
        file_bytes = np.asarray(bytearray(dog_image.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        # Display the original image (BGR format)
        st.image(opencv_image, channels="BGR")

        # Resize the image to the required size
        opencv_image = cv2.resize(opencv_image, (224, 224))
        
        # (Optional) Normalize the image if your model expects pixel values in [0, 1]
        # opencv_image = opencv_image / 255.0

        # Convert image to 4 dimensions (batch size of 1)
        opencv_image = np.expand_dims(opencv_image, axis=0)

        # Make prediction
        Y_pred = model.predict(opencv_image)
        
        # Display the predicted class
        predicted_class = CLASS_NAMES[np.argmax(Y_pred)]
        st.title("The Dog Breed is " + predicted_class)
    else:
        st.warning("Please upload an image!")
