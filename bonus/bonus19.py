import streamlit as st
from PIL import Image

# open the camera and take photo

with st.expander('state camera'):
    camera_image = st.camera_input('camera')
    print(camera_image)

# convert image to gray
img = Image.open(camera_image)
gray_img = img.convert('L')

# display the image
st.image(gray_img)
