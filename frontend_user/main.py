# frontend/main.py


import uuid
#import cv2
#import requests
import streamlit as st

import config_user as cu

LEVELS = {
    "Class": "class",
    "order": "order",   
    "family": "family",
    "genus": "genus",
    "species": "species",
}

# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("Mushroom recongnition")

# displays a file uploader widget
image = st.file_uploader("Choose an image")

# displays the select widget for the styles
level = st.selectbox("Choose a level of recognition", [i for i in LEVELS.keys()])

# displays a button
if st.button("Start recognition"):
    if image is not None and level is not None:
        files = {"file": image.getvalue()}
        name = f"IMG_PATH/{str(uuid.uuid4())}.jpg"
        #cv2.imwrite(name, files)
        #res = requests.post(f"http://backend_classif:8082/{level}", files=files)
        st.image(files, width=500)
