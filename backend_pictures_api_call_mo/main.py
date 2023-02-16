import pandas as pd
import requests
import os
import zipfile
import time
from pathlib import Path
import shutil

print('hello')

# create a Path object with the path to the file
path_file = Path('images_names.csv')
path_volume_with_csv = Path('volume_backend/images_names.csv')
path_volume_without_csv = Path('volume_backend')
print(path_file)
print(path_file.is_file())

def move_file(path_file):
    """path could either be relative or absolute. """
    # check if file or directory exists
    if path_file.is_file() or path_file.is_file():
        # move file
        shutil.move(path_file, path_volume_without_csv)
    else:
        raise ValueError("Path {} is not a file or dir.".format(path_file))


# def delete_file(path_file):
#     """path could either be relative or absolute. """
#     # check if file or directory exists
#     if path_file.is_file():
#         # remove file
#         os.remove(path_file)
#     elif path_file.is_file():
#         # remove directory and all its content
#         shutil.rmtree(path_file)
#     else:
#         raise ValueError("Path {} is not a file or dir.".format(path_file))


if path_file.is_file() == True:
    move_file(path_file)
    # delete_file(path_file)
    print('CSV moved in volume')
elif path_volume_with_csv.is_file() == True:
    print('CSV present in the volume')
else : raise ValueError('CSV file is absent from build repertory (host machine) or volume : images_names.csv')


df = pd.read_csv('volume_backend/images_names.csv')

df = df.sample(200)

PATHs = 'https://images.mushroomobserver.org/320/'

path_temp_id = df.image_id.values
names = ['{0}.jpg'.format(path_temp_ids) for path_temp_ids in path_temp_id]

urls = [PATHs+'{0}.jpg'.format(path) for path in path_temp_id]


start_time = time.time()
with zipfile.ZipFile(str(path_volume_without_csv)+'/Images_MO.zip', 'w') as img_zip:
    for image_url,name in zip(urls,names):
        img_name = name
        img_data = requests.get(image_url).content
        img_zip.writestr(img_name, img_data)
        
et = time.time()

print('execution time',et-start_time)


# docker image build . -t my_image:latest
# docker container run -it --name plop --mount type=volume,src=Image_MO,dst=/app/image_mo_container my_image:latest