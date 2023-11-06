import ray
import time
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
ray.init()

@ray.remote
def pixel3(imgpath):
    img = Image.open(imgpath)
    pixels = img.load()
    tup = img.size
    w = tup[0]
    h = tup[1]
    for i in range(w):
        for j in range(h):
            if (i + j) % 3 == 0:
                pixels[i, j] = (0, 0, 0)
    return imgpath

@ray.remote
def filter23(imgpath):
    img = Image.open(imgpath)
    pixels = img.load()
    w,h = img.size
    if pixels[2, 3][0] > 1:
        img = None
    return imgpath
     

class Collection:
    def __init__(self, path) -> None:
        self.path = path
        self.list = os.listdir(path)
        for i in range(len(self.list)):
            self.list[i] = '/home/vatsal/temp/Dataset/' + self.list[i]
        
            
        
    def print_geo(self):
        print(ray.get(self.list))
        return
        
    def map_geo(self, func, data_list):
        temp_coll = Collection(self.path)
        temp_coll.list = [func.remote(x) for x in data_list]
        return temp_coll

    

