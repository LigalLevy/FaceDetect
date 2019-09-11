import os
import shutil

from pip._vendor import requests


def download_img(url):
    base_folder = os.path.dirname(os.path.realpath(__file__))
    downloads_path = os.path.join(base_folder, 'downloads')
    if not os.path.exists(downloads_path):
        os.makedirs(downloads_path)
    pic = url.split('/')
    pic_filename = pic[-1]
    picture_path = os.path.join(downloads_path, pic_filename)
    r = requests.get(
        url,
        stream=True,
    )
    if r.status_code == 200:
        with open(picture_path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    return picture_path
