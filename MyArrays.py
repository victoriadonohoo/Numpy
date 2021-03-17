import numpy as np 
import random 

integers = np.array([1,2,3])

print(type(integers))

#LIST COMPREHENSION 
#Create a one dimensional array from a list comprehension that 
# produces even integers from 2 through 20 

integers = np.array([x for x in range(2,21,2)])
print(integers) 

floats = np.array([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7])
print(floats)

#LIST COMPREHENSION 
#Create a two dimensional array from a list comprehension that 
# produces even integers from 2 through 20 

integers = np.array([[2,21,2],[4,5,6]])
print(integers) 

a = integers.dtype
b = integers.ndim 
c = integers.shape 
d = integers.size 

print()


for row in integers:
    print(row)
    for col in row:
        print(col, end=' ')


for i in integers.flat:
    print(i)

# EXERCISE 

# create a 2 dimensional array of 5 integer elements each using the 
#   random module and list comprehension print out its dimension 
#   shape and size 


integers = np.array([[1,2,3], [4, 5, 6]])
a = np.array([[random.randint(1,10) for x in range (5)], 
              [random.randint(1,10) for x in range(5)]])

# using the np random module is easier:
b = np.array(np.random.randint(1,10,size=(2,5)))

print()

# creating an array of 5 elements that are all zero 
c = np.zeros(5)

# creating an array of 5 elements that are all one 
d = np.ones(5)

# creates a two dimensional array of 4 elements each that are all one and are integers 
e = np.ones((2, 4), dtype=int)

# create an array of specified numbers 
f = np.full((3,5), 13)

# creates an array of elements from 0 to 4 
g = np.arange(5)

# creates an array from the range 5-10 
h = np.arange(5, 10)

# creates an array ... 
i = np.arange(10, 1, -2)

print()


# evenly spaced float range 
print(np.linspace(0.0, 1.0, num=5)) 


array1 = np.arange(1,21)
array2 = array1.reshape(4,5)

print(array1)
print(array2)



array3 = np.arange(1, 100001).reshape(4, 25000)

print(array3)

array4 = np.arange(1, 100001).reshape(100, 1000)

print(array4)



numbers = np.arange(1, 6)

numbers += 10 

print(numbers)

print(numbers * 2)

print(numbers ** 3)

# numbers is unchanged by the arithmetic operators 
print(numbers)

# multiplying integer arrays with floating point arrays 
#   result is a floating point array 
numbers2 = np.linspace(1.1, 5.5, 5)

print(numbers * numbers2)

print(numbers >= 13)
print(numbers2 < numbers)
print(numbers == numbers2)