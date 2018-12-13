import requests


def get_image_from_file(filename):  #graping image file directly
    with open(filename,'rb') as imgfile:
        return imgfile.read()
