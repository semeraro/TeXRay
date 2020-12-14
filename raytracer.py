# experiment with the txr package. Build a raytracer.
# import the ray class
import sys 
sys.path.append("c:\\Users\\Dave Semeraro\\Documents\\TeXRay")
from txr.render import rays, image
import matplotlib.pyplot as plt
from PIL import Image
#%matplotlib inline
import numpy as np
#
# Going to need an image
#
height = 100
width = 200
myimage = image.image(height,width)
#
# now we are going to need some rays
# we are going to need a list of origins and directions
#
origins = []
directions = []
#
# set our view point to be the origin of the global coordinates
# set the up direction to be positive y, right to be positive x
# and set the view direction to be the negative z direction. 
# 
up = np.array((0.,1.,0.),dtype=np.float)
eye = np.array((0.,0.,0.),dtype=np.float)
#
# now we need a viewport which we place at z = -1
# 
lower_left = np.array((-2.0,-1.0,-1.0))
# direction vectors left-right down-up
horiz = np.array((4.0,0.,0.))
vert = np.array((0.,2.,0.))
# set the origins and directions so we can use them to generate ray data
for i in range(height):
    for j in range(width):
        origins.append(eye)
        u = float(j)/float(width)
        v = float(i)/float(height)
        direction = lower_left + u*horiz +v*vert 
        directions.append(direction)
raygen = rays.ray_generator(origins,directions)
# use the ray generator to make rays
raygen.generate()
# get the ray group container from the generator
rayGroup = raygen.ray_group
print(f'ray group has {rayGroup.numrays} rays')
#
# How about a ray intersection function.
#
def hit_sphere(r,center,radius):
    oc = r.origin - center
    a = np.dot(r.direction , r.direction)
    b = 2.0*np.dot(oc,r.direction)
    c = np.dot(oc,oc) - radius*radius
    disc = b*b -4.0*a*c
    return (disc > 0)
#
def color(r):
    center = np.array((0.,0.,-1.))
    radius = 0.5
    if hit_sphere(r,center,radius):
        return((255,0,0))
    else:
        return((0,0,255))
#
# use these functions to trace a group of rays
# use the image ordering of [row,column] "c" order
for row in range(height):
    for column in range(width):
        index = width*row + column # index into raydata
        rayGroupData = rayGroup[index]
        origin = rayGroupData[0:3]
        direction = rayGroupData[3:6]
        t = rayGroupData[8]
        #create new ray object with data from indexed ray
        r = rays.ray(origin,direction,t)
        #set payload to color
        r.payload = color(r)
        rayGroup[index] = r.raydata
#
# copy raygroup data over to the image
#
print(rayGroup[:,9:12].reshape((height,width,3)).shape)
print(myimage[:].shape)
myimage[:,:] = rayGroup[:,9:12].reshape((height,width,3))
# display the image
Image.fromarray(myimage[:,:]).show()