

# AMatrix multiplication using numpy

import numpy as np
a=np.array([1,2,3,4,5,6])
b=np.array([4,5,6,7,8,9])
a.shape=(3,2)
b.shape=(2,3)
c=np.dot(a,b)
print ("\nMatrix multiplication Result: ")
print (c ) 
# Vector cross product
d=np.array([1,2,3])
e=np.array([4,5,6])
f=np.cross(d,e)
print ("\nCross product Result: ")
print (f)
# Scalar triple product
g=np.array([1,2,3])
h=np.array([4,5,6])
i=np.array([7,8,10])
k=np.vdot(g,np.cross(h,i))      # This one is actually looks like g.(h*i) which gives the volume of a parallelopiped
print ("\nScalar Triple Product Result: ")
print (k)
'''output
Matrix multiplication Result: 
[[18 21 24]
 [40 47 54]
 [62 73 84]]
Cross product Result: 
[-3  6 -3]
Scalar Triple Product Result: 
-3
'''
