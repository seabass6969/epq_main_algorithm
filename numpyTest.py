import numpy

numbers = numpy.array([[1,2,5], [3,2,1], [1,3,2]])
bool_mask = numbers >= 3
x, y = bool_mask.nonzero()
# print(x,y)
# print(numbers[:,1])
print(numbers[x, y])
