import ray
import time
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
ray.init()

@ray.remote
def pixel3(img):
    pixels = img.load()
    tup = img.size
    w = tup[0]
    h = tup[1]
    for i in range(w):
        for j in range(h):
            if (i + j) % 3 == 0:
                pixels[i, j] = (0, 0, 0)
    return img

@ray.remote
def filter23(img):
    pixels = img.load()
    w,h = img.size
    if pixels[2, 3][0] > 1:
        img = None
    return img
     
@ray.remote
def ext(imgpath):
    img = Image.open(imgpath)
    return img
        

class Collection:
    def __init__(self, path) -> None:
        self.path = path
        self.list = os.listdir(path)
        for i in range(len(self.list)):
            self.list[i] = '/home/vatsal/temp/Dataset/' + self.list[i]
        
    def extract(self):
        return [ext.remote(x) for x in self.list]
            
        
    def print_geo(self,list):
        print(ray.get(list))
        return
        
    def map_geo(self, func, data_list):
        return [func.remote(x) for x in data_list]


    

