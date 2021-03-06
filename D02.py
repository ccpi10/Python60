import numpy as np

array1=np.array(range(30))
a2=np.reshape(array1,(5,6),order='F')
print(a2)

a3=np.where(array1%6==1)
print(a3)

#print(help(np.reshape))
