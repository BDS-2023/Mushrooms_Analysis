import pandas as pd
import requests
import os
import zipfile
import time
from pathlib import Path
import shutil

print('hello')
# df = pd.read_csv('/var/lib/docker/volumes/Image_MO/_data/images_names.csv')

# create a Path object with the path to the file
path_file = Path('images_names.csv')
path_volume = 'volume_backend'


def move_file(path):
    """path could either be relative or absolute. """
    # check if file or directory exists
    if os.path.isfile(path) or os.path.islink(path) or os.path.isdir(path):
        # move file
        shutil.move(path, path_volume)
    else:
        raise ValueError("Path {} is not a file or dir.".format(path))


def delete_file(path):
    """path could either be relative or absolute. """
    # check if file or directory exists
    if os.path.isfile(path) or os.path.islink(path):
        # remove file
        os.remove(path)
    elif os.path.isdir(path):
        # remove directory and all its content
        shutil.rmtree(path)
    else:
        raise ValueError("Path {} is not a file or dir.".format(path))


if os.path.isfile(path_file) == True:
    move_file(path_file)
    delete_file(path_file)
elif os.path.isfile(path_volume/path_file) == True:
    print('CSV present in the volume')
else : raise ValueError('CSV file is absent from build repertory (host machine) or volume : images_names.csv')


df = pd.read_csv('volume_backend/images_names.csv')

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