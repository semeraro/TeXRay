"""
Some useful decorators. 
"""
import functools
import time
import sys

def timer(func):
    """ time a function """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    
    return wrapper_timer

def debug(func):
    """ dump out some info on this function"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ",".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    
    return wrapper_debug

def has_module(mod_name=None):
    def decorator_modcheck(func):
        @functools.wraps(func)
        def wrapper_modcheck(*args,**kwargs):
            print(f'mod_name is {mod_name}')
            print(f'dir -> {dir()}')
            print(f'locals -> {tryit.locals()}')
            print(f'yourmama =============')
            if (mod_name in sys.modules) and (mod_name in dir()):
                location = os.getcwd()
                print(f'calling {func.__name__} from {location}')
                value = func(*args,**kwargs)
            else:
                print(f'calling {func.__name__} from nowhere')
                value = None
            return value
        return wrapper_modcheck
    return decorator_modcheck

