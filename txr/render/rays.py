"""module with ray related stuff in it"""
#import numpy as np
from numpy import ndarray,finfo,iinfo,zeros,array,zeros_like
#
class ray:
    """ a ray class that uses numpy"""
    def __init__(self, origin,direction):
        self._tmin = finfo('float32').min
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

class ray_group:
    """ 
    a group of rays 
    
    The data is stored in a numpy array with numrays rows and enough
    columns to store the ray data"""
    def __init__(self,numrays = None):
        if numrays is None:
            self._rays = None
        else:
            self._rays = zeros((numrays,12),dtype='float32')

    def add_ray(self,ray):
        self._rays.append(ray)

    def add_rays(self,rays):
        self._rays.extend(rays)

    @property
    def rays(self):
        return self._rays

    