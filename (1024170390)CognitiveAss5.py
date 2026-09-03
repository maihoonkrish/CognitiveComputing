#Q1
print("Q1")

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Addition of 2 to all element :", arr + 2)

print("Multiplication of 3 to all element :", arr * 3)

print("Division of 2 to all element :", arr / 2)


#Q2(a)
print("Q2(a)")

arr = np.array([1, 2, 3, 6, 4, 5])

reverse = arr[::-1]

print("Original array:", arr)
print("Reversed array:", reverse)


#Q2b(i)
print("Q2b(i)")

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])

values, counts = np.unique(x, return_counts=True)

most_frequent = values[np.argmax(counts)]

indices = np.where(x == most_frequent)[0]

print("Array:", x)
print("Most frequent value:", most_frequent)
print("Frequency:", np.max(counts))
print("Indices:", indices)


#Q2b(ii)
print("Q2b(ii)")

y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

values, counts = np.unique(y, return_counts=True)

max_frequency = np.max(counts)

most_frequent = values[counts == max_frequency]

print("Array:", y)
print("Most frequent values:", most_frequent)
print("Frequency:", max_frequency)

for value in most_frequent:
    indices = np.where(y == value)[0]
    print("Indices of", value, ":", indices)


#Q3
print("Q3")

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("1st row, 2nd column:", arr[0, 1])

print("3rd row, 1st column:", arr[2, 0])


#Q4
print("Q4")

Krish = np.linspace(10, 100, 25)

print("Array:")
print(Krish)

print("Dimensions:", Krish.ndim)

print("Shape:", Krish.shape)

print("Total elements:", Krish.size)

print("Data type:", Krish.dtype)

print("Total bytes:", Krish.nbytes)

reshaped = Krish.reshape(25, 1)

print("Array after reshape:")
print(reshaped)

transpose = reshaped.T

print("Transpose using reshape():")
print(transpose)

print("Using T attribute:")
print(reshaped.T)


#Q5
print("Q5")

ucs420_Krish = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 15, 20, 35]
])

print("Original Array:")
print(ucs420_Krish)

print("Mean:", np.mean(ucs420_Krish))

print("Median:", np.median(ucs420_Krish))

print("Maximum:", np.max(ucs420_Krish))

print("Minimum:", np.min(ucs420_Krish))

print("Unique elements:", np.unique(ucs420_Krish))


reshaped_ucs420_Krish = ucs420_Krish.reshape(4, 3)

print("Reshaped Array (4 x 3):")
print(reshaped_ucs420_Krish)


resized_ucs420_Krish = np.resize(ucs420_Krish, (2, 3))

print("Resized Array (2 x 3):")
print(resized_ucs420_Krish)