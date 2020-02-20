""" test module with an example function """
import numpy as np
from txr.render import rays
orig = np.array([0.0,0.0,0.0])
direct = np.array([1.0,1.0,1.0])
r1 = rays.ray(orig,direct)
print(f'{r1.origin}, {r1.direction}')
print(f'{r1.pt_at_t(0.5)}')