"""Image related code"""
import numpy as np
from PIL import Image,ImageOps
import os
import sys
import copy, math
class image:
    """
    A numpy based image container. The image resides in a numpy array

    
    """
    def __init__(self,height=100,width=200):
        self._width = width
        self._height = height
        self._data = np.zeros((height,width,3),dtype=np.uint8)
    
    def __getitem__(self,key):
        return self._data[key]
    def __setitem__(self,key,value):
        self._data[key] = value
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height