import ray
import time
import numpy as np
import matplotlib.pyplot as plt

class Image:
    def __init__(self, path) -> None:  ## Give it a path to a image
        self.timestamp = time.time()
        self.pixels = 0
    
    def print_geo(self):
        pass
    
    def clip(self):
        pass
    
    def reduce(self, **kwargs): ## kwargs : options for reduce_geo
        pass
    
    def getinfo(self):
        pass

class Collection:
    def __init__(self, path) -> None:
        self.timestamp = time.time()
        self.images = []
        
    def print_geo(self):
        pass

    def reduce(self, **kwargs): ## kwargs : options for reduce_geo
        pass
    
    def getinfo(self):
        pass
    
class randomforest:
    pass

class svm:
    pass

class nn:
    pass


