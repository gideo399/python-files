import numpy as np


#accessing /changing specific element ,rows,columns etc 


a=np.array([[1,2,3,4,5,6,7],[5,4,32,56,32,4,6]])
print(a)
#get a specific number [r,e]
print(a[1,5])
#get aspecific row 
print(a[1,:])
#get a specific column
print(a[:,2])
#get alittle more fancy
print(a[1  ,1:6:2])

#change any number in an array 

print(np.random.randint(7, size=(3,3)))
  
  
print(np.identity(5))


q=np.genfromtxt('data.txt', delimiter=',')
print(q)




























