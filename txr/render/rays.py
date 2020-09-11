"""module with ray related stuff in it"""
#import numpy as np
from numpy import ndarray,finfo,iinfo,zeros,array,zeros_like,empty
import copy
#
class ray:
    """ 
    a single ray with data stored in a numpy array (vector)
    The data is stored in a contiguous vector
    
    ...

    Attributes
    ----------

    origin : numpy array
        The origin of the ray. 

    direction : numpy array
        The direction of the array. Not necessarily a unit vector

    payload : numpy array
        A three element vector containing the "value" of the ray. It could 
        contain color or any other three element vector associated with the ray.

    t : float 
        The parameter measuring distance along the ray from the origin. 

    ...

    Methods
    -------

    pt_at_t(t) : returns the point on the ray a distance t from the origin
        changes the current value of t in the vector.

    """
    def __init__(self, origin,direction):
        self._data = zeros(12)
        self._data[0:3] = origin
        self._data[3:6] = direction 
        self._data[6] = finfo('float32').tiny
        self._data[7] = finfo('float32').max
        self._data[8] = self._data[6]  
    def pt_at_t(self,t=None):
        if t is not None:
            self._data[6] = t 
        return self._data[0:3] + self._data[6]*self._data[3:6]
    @property
    def origin(self):
        return self._data[0:3]
        #return self._origin
    @property
    def direction(self):
        return self._data[3:6]
        #return self._direction
    @property
    def t(self):
        return self._data[8]
        #return self._t
    @property
    def payload(self):
        return self._data[9:12]
    @property
    def alldata(self):
        return self._data[:]

class ray_group:
    """ 
    a group of rays 
    
    The data is stored in a numpy array with numrays rows and enough
    columns to store the ray data
    
    ...

    Attributes
    ----------
    rays : numpy array
        A numpy array containing all the rays in this broup
    
    Methods
    -------
    insert_ray(ray) : Appends ray to array

    add_rays(rays) : Appends a bunch of rays to the numpy array.

    """

    def __init__(self,numrays = None):
        """ 
        Parameters
        ----------
        numrays : The number of rays to allocate in this group
            If numrays is None then an empty ray group results.

        """

        if numrays is None:
            self._rays = empty((1,12),dtype='float32')
        else:
            self._rays = zeros((numrays,12),dtype='float32')
        self._current_position = 0
        print(f'ray_group rays.shape {self._rays.shape}')

    def insert_ray(self,ray,position=0):
        """ Add a ray to the group.

        Inserts a ray in the current position of the array. Overwrites the
        data in that position with the data in ray. Insert into position if 
        given. Advances current position counter by one. Sets current position
        counter to position + 1 if position given. 
        
        Parameters
        ----------
        ray : A txr.rays.ray object 
        position : row number of the numpy array to insert data into
        """

        self._rays.append(ray)

    def set_ray(self,ray,position):
        """ Overwrite the values of the ray 
        
        Overwrite the ray data in position given 
        with the new values in ray. 

        Parameters
        ----------
        ray : A txr.rays.ray object
        position : The row of the ray group that
            will be overwritten.
        """

        self._rays[position,:] = ray.alldata

    def add_rays(self,rays):
        self._rays.extend(rays)

    @property
    def rays(self):
        return self._rays

class ray_generator:
    """
    This class generates rays given origin data and direction data

    The class returns a ray_group. The input origin can be any iterable 
    object that returns x,y,z tuples. The same goes for direction.

    """
    def __init__(self,origin,direction):
        #the number of rays in the group is the number of origins
        numrays = len(origin)
        _raygrp = ray_group(numrays=numrays)
        
        print(f'{numrays}')
        #for orig,dir in map(none,origin,direction):
        #    print(f'{orig}, {dir}')
    