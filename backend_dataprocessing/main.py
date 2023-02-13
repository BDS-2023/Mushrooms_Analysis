# backend_dataprocessing/main.py

import uuid

import cv2
import uvicorn
import requests
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
import datetime as dt


import update_data as upd
import dataprocessing_from_csv_MO as dpg


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API of dataprocessing"}


#activate the update calls to MO and the dataprocessing to append the csv-files
@app.post("/{date}")
def get_image(date: str, file: UploadFile = File(...)):

    return 

#activate the update of models training
@app.post("/{date}")
def get_image(date: str, file: UploadFile = File(...)):

    return 


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8082)