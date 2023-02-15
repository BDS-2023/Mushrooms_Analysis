import pandas as pd
import requests
import os
import zipfile
import time

print('hello')
# df = pd.read_csv('/var/lib/docker/volumes/Image_MO/_data/images_names.csv')

df = pd.read_csv('image_mo_container/images_names.csv')

df = df.sample(200)

PATHs = 'https://images.mushroomobserver.org/320/'

path_temp_id = df.image_id.values
names = ['{0}.jpg'.format(path_temp_ids) for path_temp_ids in path_temp_id]

urls = [PATHs+'{0}.jpg'.format(path) for path in path_temp_id]


start_time = time.time()
with zipfile.ZipFile('image_mo_container/Images_MO.zip', 'w') as img_zip:
    for image_url,name in zip(urls,names):
        img_name = name
        img_data = requests.get(image_url).content
        img_zip.writestr(img_name, img_data)
        
et = time.time()

print('execution time',et-start_time)


# docker image build . -t my_image:latest
# docker container run -it --name plop --mount type=volume,src=Image_MO,dst=/app/image_mo_container my_image:latest