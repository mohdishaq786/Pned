import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img 
from tensorflow.keras.models import load_model
import os
from skimage.io import imread
from skimage.transform import resize

from tensorflow.keras.optimizers import Adam

from PIL import Image
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

ref_lab={0 :'NORMAL', 1 :'PNEUMONIA'}
model = load_model('model.h5', compile = False)

st.title('Pneumonia Detector')

st.image('https://upload.wikimedia.org/wikipedia/commons/8/81/Chest_radiograph_in_influensa_and_H_influenzae%2C_posteroanterior%2C_annotated.jpg', width = 500)
st.text('Please upload the Chest X-ray')

choice = st.selectbox('Choose one of the following', ('URL', 'Upload Image'))
try:
  if choice == 'URL':
    image_path = st.text_input('Enter image URL...')
    try:
      img = imread(image_path)
      img = resize(img, (256, 256))/255
    except:
      st.markdown('Enter a URL')

  if choice == 'Upload Image':
    img = st.file_uploader('Upload an Image')
    try:
      img = Image.open(img)
      img = np.array(img)/255
      img = resize(img, (256, 256))
      
    except:
        st.markdown('Upload a valid image')

  pred = model.predict(np.expand_dims(img, 0))[0]
  pred=int(pred>0.8)
  pred= lab.get(pred)
  
    
  text = st.text_area(pred, height=300) 

  st.image(img, caption = 'Input', width = 256)
  
except:
  pass
