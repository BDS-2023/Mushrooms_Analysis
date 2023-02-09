# backend_CNN/main.py

import uuid

import cv2
import uvicorn
import requests
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
from PIL import Image
import datetime as dt


import cnn


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API of CNN ! The core of Deep Learning"}


@app.post("/Update")
def get_image():

    return 


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081)