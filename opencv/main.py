#How to Match an Image That Is Embedded in Another Image in Python using OpenCV
import io
import streamlit as st
from PIL import Image
import cv2
import numpy as np


st.title('Template Matching Using OPENCV in Python')
st.code('while(1):pikachuuu')

st.subheader('My sub')
st.text('Description')
st.text('Select a picture from the sidebar')


selected_box = st.sidebar.selectbox(
'Choose an image',
('1','2','3','4','5')
)
if selected_box == '1':
    template = '23.png'
if selected_box == '2':
    template = '2.png'
if selected_box == '3':
    template = '4.png'
if selected_box == '4':
    template = '17.png'
if selected_box == '5':
    template = '18.png'


st.image(template)
template= cv2.imread(template,0)

image= cv2.imread('pokemon3.png')
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
result= cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(result)

height, width= template.shape[:2]

top_left= max_loc
bottom_right= (top_left[0] + width, top_left[1] + height)
cv2.rectangle(image, top_left, bottom_right, (0,0,255),5)

#cv2.imshow('Pokemon', image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

st.image(image)


if (st.button("Run")):
    with st.echo(code_location='below'):

        st.image(template)
        template= cv2.imread(template,0)
        
        image= cv2.imread('pokemon3.png')
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        result= cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(result)

        height, width= template.shape[:2]

        top_left= max_loc
        bottom_right= (top_left[0] + width, top_left[1] + height)
        cv2.rectangle(image, top_left, bottom_right, (0,0,255),5)

