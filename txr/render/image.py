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
        newkey = self._reverse_height_index(key)
        self._data[newkey] = value 
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    def _reverse_height_index(self,key):
        """ internal method to adjust the row index to count from
        the bottom of the array instead of the top. This insures the
        image is indexed from the bottom left corner. 
        """
        # this reverses the height index value
        if isinstance(key,int):  # got a single index. 
            newkey = self._height - key -1 
            return newkey
        if isinstance(key,tuple): # we have multiple indices
            keylist = list(key) # create a mutable object
            if isinstance(keylist[0],int): 
                # first element is int
                keylist[0] = self._height - key[0] -1
                newkey = tuple(keylist)
            elif isinstance(keylist[0],slice): 
                # first element is slice
                if keylist[0].start is None:
                    start = self._height -1
                else:
                    start = self._height - 1 - key[0].start 
                if keylist[0].stop is None:
                    stop = None
                else:
                    stop = self._height-key[0].stop -1
                if key[0].step is None:
                    step = -1
                else:
                    step = -key[0].step
                keylist[0] = slice(start,stop,step)
                newkey = tuple(keylist)
            return newkey