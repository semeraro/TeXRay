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
import decorators
#from decorators import debug
#from decorators import has_module
def has_gvt(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        obj = args[0]
        #obj._hasgvt = True
        try:
            import gvt
        except ImportError as ex:
            obj._hasgvt = False
            #print(ex)
        except ValueError as ex:
            obj._hasgvt = False
            #print(ex)
        else:
            obj._hasgvt = True
        return func(*args,**kwargs)
    return wrapper

@decorators.debug
def make_greeting(name,age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Howdy {name} you are {age}"

@decorators.has_module(mod_name='os')
def im_in():
    return f'module os loaded'

class Some:
    @decorators.debug
    def __init__(self,max_num):
        self.max_num = max_num

    @decorators.debug
    def get_some(self):
        return(self.max_num)
    @has_gvt
    def render(self):
        return(self._hasgvt)

#def main():
#    make_greeting("dave")
#    make_greeting("dave",age=61)
#im_in()
#print(f'tryit locals -> {locals()}')
A = Some(10)
print(f' A has gvt {A.render()}')
    #B = Some(30)
    #print(f"A has {A.get_some()} things B has {B.get_some()} things")

#if __name__ == "__main__":
#    main()