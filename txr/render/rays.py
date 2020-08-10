"""module with ray related stuff in it"""
#import numpy as np
from numpy import ndarray,finfo,iinfo,zeros,array,zeros_like
#
class ray:
    """ a ray class that uses numpy"""
    def __init__(self, origin,direction):
        self._tmin = finfo('float32').tiny
        self._tmax = finfo('float32').max
        self._t = self._tmin
        self._payload = zeros_like(origin,dtype='float32')
        if isinstance(origin,ndarray):
            self._origin = origin.copy()
        if isinstance(direction,ndarray):    
            self._direction = direction.copy()
    def pt_at_t(self,t):
        return self._origin + t*self._direction
    @property
    def origin(self):
        return self._origin
    @property
    def direction(self):
        return self._direction
    @property
    def t(self):
        return self._t

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

        """

        if numrays is None:
            self._rays = None
        else:
            self._rays = zeros((numrays,12),dtype='float32')
        self._current_position = 0

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
        
        print(f'{numrays}')
        for item in origin:
            print(f'{item}')
    