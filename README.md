# TeXRay
Ray tracing experiments done at TACC/University of Texas. This repo contains experiments in ray tracing for scientific visualization that I did while at the University of Texas. I set this up to do experimental things before I folded them into "production" code that came out of my group (Scalable Visualization Technologies). 
## Utilities
The repo contains utility code that is not specifically related to ray tracing but comes in handy. Every effort has been made to reduce use
of third party libs when it is not necessary. However sometimes it is just easier or necessary to utilize what is available. For example, IO with hdf is just so convenient that it is hard not to utilize it. 
### Vectors and Math 
Every ray tracing code uses some  sort of vector class with accompanying matrix multiplication (transform) class. This code is generic and can be used for many other graphics purposes. I could use the glm code for this and I will support that option but I like to reduce the amount of thirdparty depennds. Vector code is very easy to write and having it in the source tree makes it easy to examine to  see how it
works. As a first pass we are using numbpy. 
### Data Import
Gotta read the data. There are some data reading bits here. Some are written by me and others are third party. Reading obj for example
is supported by multiple sources of reader. 
### Image export
Third party image libs of various forms are readily available. I include them where appropriate. I also include a ppm writer. 
## Parallelism
One of the main reasons for creatng this work is to experimant with parallelism for ray tracing. There are three levels of parallelism
in a distributed application, MPI message passing, multithreading, and vectorization. I want to compare different forms of parallelism 
to see how each performs. For example I want to compare TBB with openmp with the aim of evaluating speed vs ease of use. 
## Vectorization
Vector units are an important part of modern processor arch and I have some experiments in how the use of vectorization can impact the speed of the code. Vectorization is impacted by the data structures more than any other form of parallelism. I want to determine the impact of SOA and AOS and in particular to determine if converting from one to the other is an option with the code. 
## Test Data
You gotta have test data. Some geometric and some scientific data of small size will be included. Links to larger datasets publicly available will also be included. 
## Rendering
This is the fun bit. Here I esperiment with lighting, shadows, attenuation, and all the other bits and pieces that make ray tracing fun.
