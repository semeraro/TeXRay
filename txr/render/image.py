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
        """ internal method to adjust the row index to count from
        the bottom of the array instead of the top. This insures the
        image is indexed from the bottom left corner. 
        """
        # this reverses the height index value
        if isinstance(key,int):  # got a single index. 
            newkey = self._height - key -1 
            return newkey
        if isinstance(key,tuple): # we have multiple indices
            if isinstance(key[0],int):
                keylist  = list(key)
                keylist[0] = self._height - key[0] -1
                newkey = tuple(keylist)
            elif isinstance(key[0],slice):
                keylist = list(key)
                start = self._height - key[0].start -1
                stop = self._height - key[0].stop -1 
                step = (key[0].step,-1)[key[0].step is None]
                keylist[0] = slice(start,stop,step)
                newkey = tuple(keylist)
            return newkey