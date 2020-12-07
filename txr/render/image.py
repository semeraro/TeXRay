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
        print(f'length of input tuple {len(key)}')
        newkey = self._reverse_height_index(key)
        print(f'{newkey}')
        return self._data[newkey,:]
        #return self._data[key]
    def __setitem__(self,key,value):
        self._data[self._height - key[0] -1,key[1]] = value
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    def _reverse_height_index(self,key):
        # this reverses the height index value
        print(key[0].step)
        print(('no','yes')[key[0].step is None])
        if isinstance(key[0],slice): # got a slice
            key0 = slice(self._height - key[0].start -1,\
                             self._height - key[0].stop  -1,\
                              (-(key[0].step),None)[key[0].step is None])
        else:
            key0 = self._height - key[0] - 1
        if len(key) < 3:
            return (key0,key[1])
        else:
            return (key0,key[1],key[2])