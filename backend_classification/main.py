# backend/main.py

import uuid

import cv2
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
from PIL import Image

import config_classif as config
import classification as clf


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API of classification"}


@app.post("/{level}")
def get_image(level: str, file: UploadFile = File(...)):
    image = np.array(Image.open(file.file))
    model = config.LEVEL[level]
    output, image  = clf.classification(model, image)
    name = f"/storage/{str(uuid.uuid4())}.jpg"
    cv2.imwrite(name, output)
    return {"name": name}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)