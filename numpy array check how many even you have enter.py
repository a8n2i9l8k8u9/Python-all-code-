import numpy as np
arr=np.array([0,1,2,3,4,5,6])
c=0
for i in arr:
    if(arr[i]%2==0):
        c=c+1
print(c)
