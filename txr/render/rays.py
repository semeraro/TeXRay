"""module with ray related stuff in it"""
#import numpy as np
from numpy import ndarray,finfo,iinfo,zeros,array,zeros_like,empty,append
import copy
import math
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

    normalize(): makes the direction of this ray a unit vector

    """
    def __init__(self, origin,direction,size=12):
        assert(size > 11,"ray requires 12 elements or more")
        self._data = zeros(max(size,12))
        # all rays contain at least the following data.
        # rays derived from this one may have additional
        # data.
        self._data[0:3] = origin
        self._data[3:6] = direction 
        # range of t values
        self._data[6] = finfo('float32').tiny
        self._data[7] = finfo('float32').max
        # initialize t to tiny.
        self._data[8] = self._data[6] 
    def pt_at_t(self,t=None):
        if t is not None:
            self._data[6] = t 
        return self._data[0:3] + self._data[6]*self._data[3:6]
    def normalize(self):
        len = math.sqrt(self._data[3]**2+self._data[4]**2+self._data[5]**2)
        # stick an assert in here to catch zero division
        assert len > 0.0 , "ray normalization failed"
        self._data[3:6] = self._data[3:6]/len 
    @property
    def origin(self):
        return self._data[0:3]
    @origin.setter
    def origin(self,value):
        self._data[0:3]=value[:]
    @property
    def direction(self):
        return self._data[3:6]
    @direction.setter
    def direction(self,value):
        self._data[3:6] = value[:]
    @property
    def t(self):
        return self._data[8]
    @t.setter
    def t(self,value):
        self._data[8] = value
    @property
    def payload(self):
        return self._data[9:12]
    @payload.setter
    def payload(self,value):
        self._data[9:12] = value[:]
    @property
    def raydata(self):
        return self._data[:]
    @raydata.setter
    def raydata(self,value):
        self._data[:] = value[:]


class ray_group:
    """ 
    data associated with a group of rays 
    
    This class stored data associated with a collection of rays. The
    data is stored in a numpy array. The data for one ray constitutes 
    one row of the data. Ray objects themselves are not stored, only 
    the data associated with the ray such as origin,direction, etc.
    
    ...

    Attributes
    ----------
    rays : numpy array
        A numpy array containing data for all the rays in this broup
    
    Methods
    -------
    insert_ray(ray) : Appends ray to array if array is not empty.
    

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
            self._numrays = 0
        else:
            self._rays = zeros((numrays,12),dtype='float32')
            self._numrays = numrays
    def __getitem__(self,key):
        return self._rays[key]
    @property
    def numrays(self):
        return self._numrays

    def insert_ray(self,ray):
        """ Add a ray to the group.

        Adds data from ray to the rays array by appending the data
        as another row at the bottom of the array. If the group is
        empty the ray data is placed in row zero of the array.
        
        Parameters
        ----------
        ray : A txr.rays.ray object 

        """
        tmp = ray.raydata.reshape((1,12))
        if self._numrays == 0:
            self.set_ray(ray,0)
        else:
            self._rays = append(self._rays,tmp,axis=0)
        self._numrays += 1

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

        self._rays[position,:] = ray.raydata

    def add_rays(self,rays):
        """ Add several rays to the group

        Adds data from a set of rays to the rays array in this group

        Parameters
        ----------
        rays: a numpy array of shape n,12 that contains the data for n rays
        """

        self._rays = append(self._rays,rays,axis=0)

    @property
    def rays(self):
        return self._rays

class ray_generator:
    """
    This class generates rays given origin data and direction data

    The class returns a ray_group. The input origin can be any iterable 
    object that returns x,y,z tuples. The same goes for direction. The rays
    created here have t = tmin and uninitialized payload. 

    """
    def __init__(self,origins,directions):
        #the number of rays in the group is the number of directions
        # a group can have a single origin
        self._numrays = len(directions)
        self._numorigins = len(origins)
        self._directions = directions
        self._origins = origins
        self._singleOrigin=self._numorigins == 1
        self._raygrp = ray_group()
        
    @property
    def numrays(self):
        return self._numrays
    @property
    def numorigins(self):
        return self._numorigins
    @property
    def ray_group(self):
        return self._raygrp
    def generate(self):
        # generate the rays here
        directit = iter(self._directions)
        if self._singleOrigin:
            orig = self._origins[0]
        else:
            orig = iter(self._origins)
        while True:
            try:
                if self._singleOrigin:
                    r = ray(orig,next(directit))
                    self._raygrp.insert_ray(r)
                else:
                    r = ray(next(orig),next(directit))
                    self._raygrp.insert_ray(r)
            except StopIteration:
                break