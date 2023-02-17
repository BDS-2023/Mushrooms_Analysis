import pandas as pd
import requests
import os
import zipfile
import time
import boto3
import time
import numpy as np

print('hello1')

df = pd.read_csv('images_names.csv',usecols=['image_id'],index_col=0)

session = boto3.Session()
s3 = session.resource('s3')


my_bucket = s3.Bucket('imagemobucket')

# alr_in = []
# for objects in my_bucket.objects.filter(Prefix="image_mo/"):
#     try:
#         alr_in.append(int(str(objects.key).split('/')[-1][:-4]))
#     except:
#         pass

# alr_in = np.array(alr_in)

# print(alr_in)

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
    


# df = df[~df.index.isin(alr_in)]

print('hello3')

PATHs = 'https://images.mushroomobserver.org/320/'

# path_temp = df.index.values
# urls_all = [PATHs+'{0}.jpg'.format(path) for path in path_temp]

# print('hello4')

for k in range(1000):
    try:
        uplo_from_url(PATHs+'{0}.jpg'.format(df.index.values[k]))
    except:
        print('oups')




# # # docker image build . -t my_image:latest
# # # docker container run -it --name plop --mount type=volume,src=Image_MO,dst=/app/image_mo_container my_image:latest