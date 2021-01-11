"""TeXRAY data module """
class target:
    """ 
    A target is a wrapper around data that will interact
    rays with the data in a specified way. 

    ....

    Attributes
    ----------

    data: some type of data object
        The data attribute holds the particular data. It 
        could be a class or a numpy array or anything, as 
        long as the method attribute knows how to access it
        to interact with the raygroup.

    method: A function that takes data and raygroup as input
        this method applies some operation to the data for 
        each ray in the raygroup. 

    rayGroup: This is a group of rays that are passed to the 
        method and applied to the data. 

    """
    def __init__(self,data):
        # keep the data handle as we may use this 
        # target again with other rays 
        self._data = data
        self._method = None 
        self._rayGroup = None

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self,value):
        self._method = value

    @property
    def rayGroup(self):
        return self._rayGroup

    @rayGroup.setter
    def rayGroup(self,value):
        self._rayGroup = value

    def apply_method_to_data(self):
        assert(self._method is not None)
        assert(self._rayGroup is not None)
        return(self._method(self._data,self._rayGroup))
