""" 
    Test the hasgvt decorator. The decorator wraps object methods and checks
    for the presence of the gvt module before executing the method. 

    to run from command line:
        $python3 hasgvtdecor.py
        
    to run from interpreter:
        >>> exec(open("hasgvtdecor.py").read())
"""
import os,sys
# this is where gvt lives
gvtloc = os.path.join(os.path.expanduser("~"),".pve/pyGVT/lib/python3.6/site-packages/gvt-1.0.0-py3.6-linux-x86_64.egg")
# this is where numpy is
numpyloc = os.path.join(os.path.expanduser("~"),".pve/pyGVT/lib/python3.6/site-packages")
sys.path.insert(0,numpyloc)
sys.path.insert(0,gvtloc)
from functools import wraps
def can_use_gvt(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        obj = args[0]
        try:
            import gvt
        except ImportError as ex:
            obj._hasgvt = False
            obj.gvt = None
        except ValueError as ex:
            obj._hasgvt = False
            obj.gvt = None
        else:
            obj._hasgvt = True
            obj.gvt = __import__('gvt')
        return func(*args,**kwargs)
    return wrapper

class Some:
    @can_use_gvt
    def __init__(self,max_num):
        self.max_num = max_num
#        if self._hasgvt:
#            self.gvt = __import__('gvt')

    def get_some(self):
        return(self.max_num)

    def render(self):
        if self._hasgvt:
            print(f'I can use gvt plugin')
            self.gvt.gvtInit()
        else:
            print(f'No gvt- bummer')
        return(self._hasgvt)

A = Some(10)
print(f' A has gvt {A.render()}')
