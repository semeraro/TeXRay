"""module with ray related stuff in it"""
#import numpy as np
from numpy import ndarray
#
class ray:
    """ a ray class that uses numpy"""
    def __init__(self, origin,direction):
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