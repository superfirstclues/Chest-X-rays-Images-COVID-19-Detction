import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

model = keras.models.load_model('C:\\Users\\firstclues\\Desktop\\Proj\\covid_model\\mobilenet.h5')
data=[]
labels=[]
cxr_labels = ['Normal','COVID-19','Viral_Pneumonia']

def predict(image):
    image = cv2.resize(image, (224, 224))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)[0]
    predicted_label = np.argmax(prediction)
    predicted_prob = np.max(prediction) * 100

    return cxr_labels[predicted_label], predicted_prob

st.set_page_config(page_title='Chest X-ray CCOVID-19 Detector')
st.title('Chest X-ray COVID-19 PREDICTOR')
st.write('Upload a chest X-ray image and we will predict whether it shows signs of COVID-19 or not.')
uploaded_file = st.file_uploader('Choose a chest X-ray image', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    result, prob = predict(image)
    st.write('Prediction: ', result)
    st.write('Probability: {:.2f}%'.format(prob))

else:
    st.write('Please upload a chest X-ray image to make a prediction.')
