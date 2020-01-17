""" 
    this is a test. for the next sixty seconds this program will be conducting a test 
    to run from command line:
        $python3 tryit.py
        
    to run from interpreter:
        >>> exec(open("tryit.py").read())
"""
import os
import decorators
#from decorators import debug
#from decorators import has_module

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

#def main():
#    make_greeting("dave")
#    make_greeting("dave",age=61)
im_in()
print(f'tryit locals -> {locals()}')
    #A = Some(10)
    #B = Some(30)
    #print(f"A has {A.get_some()} things B has {B.get_some()} things")

#if __name__ == "__main__":
#    main()
