import pandas as pd
import requests
import os
import zipfile
import time
import boto3
import time
import numpy as np

print('hello1')

ACCESS_KEY = 'AKIA3XYCSV3OU4IIGOAS'
SECRET_KEY = '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'

session = boto3.Session()
s3 = session.resource(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)


my_bucket = s3.Bucket('imagemobucket')

alr_in = []
for objects in my_bucket.objects.filter(Prefix="image_mo/"):
    try:
        alr_in.append(int(str(objects.key).split('/')[-1][:-4]))
    except:
        pass

alr_in = np.array(alr_in)


print('hello2')

def uplo_from_url(url):
    bucket_name = 'imagemobucket'
    key_doss = 'image_mo/'
    key = key_doss + url.split('/')[-1]
    

    req_for_image = requests.get(url, stream=True)
    file_object_from_req = req_for_image.raw
    req_data = file_object_from_req.read()

    # Do the actual upload to s3
    s3.Bucket(bucket_name).put_object(Key=key, Body=req_data)
    
    


df = pd.read_csv('images_names.csv')
df = df.drop_duplicates(subset='image_id')
df = df[~df.image_id.isin(alr_in)]

print('hello3')

PATHs = 'https://images.mushroomobserver.org/320/'
path_temp = df.image_id.values
urls_all = [PATHs+'{0}.jpg'.format(path) for path in path_temp]


# for k in range(100):
#     try:
#         uplo_from_url(urls_all[k])
#     except:
#         print('oups')




# docker image build . -t my_image:latest
# docker container run -it --name plop --mount type=volume,src=Image_MO,dst=/app/image_mo_container my_image:latest