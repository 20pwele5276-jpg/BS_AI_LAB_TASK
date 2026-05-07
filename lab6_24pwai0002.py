# NumPy Lab

# importing numpy
import numpy as np
##Task 1 — Creating Arrays

print("\nTask 1 — Creating Arrays")
# 1D array
my_numbers = np.array([1,2,3,4,5,6,7,8,9,10])

# 2D array
my_matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])

# zeros array
zero_data = np.zeros((4,4))

# ones array
one_data = np.ones((2,5))

print(my_numbers)
print(my_matrix)
print(zero_data)
print(one_data)


##Task 2 — Array Properties

print("\nTask 2")
print("Shape:", my_matrix.shape)
print("Total Elements:", my_matrix.size)
print("Datatype:", my_matrix.dtype)
print("Dimensions:", my_matrix.ndim)

print("Shape is important because AI stores data in rows and columns.")



# Task 3 — Indexing

print("\nTask 3")

values = np.array([10,20,30,40,50,60])

# accessing elements
print("First value:", values[0])
print("Last value:", values[-1])
print("Third value:", values[2])

# values greater than 30
print("Values greater than 30")
print(values[values > 30])



# Task 4 — Slicing

print("\nTask 4")

# slicing
print(values[1:5])

# reverse
print(values[::-1])

# alternate values
print(values[::2])

#  for matrix
student_matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])

# first row
print("First row")
print(student_matrix[0])

# second column
print("Second column")
print(student_matrix[:,1])

# last two rows
print("Last two rows")
print(student_matrix[1:])

##Task 5 — Vectorization

print("\nTask 5")

simple_array = np.array([1,2,3,4,5])

# multiply by 5
print(simple_array * 5)

# add 10
print(simple_array + 10)

# square values
print(simple_array ** 2)

print("Vectorization makes calculations easy and fast.")



##Task 6 — Broadcasting

print("\nTask 6")

two_d_array = np.array([[1,2,3], [4,5,6]])

# add 10
print(two_d_array + 10)

# multiply by 2
print(two_d_array * 2)

print("Broadcasting helps to apply operation on full array together.")



# Task 7 — Matrix Addition and Subtraction

print("\nTask 7")

first_matrix = np.array([[1,2], [3,4]])
second_matrix = np.array([[5,6],  [7,8]])

# addition
print("Addition")
print(first_matrix + second_matrix)

# subtraction
print("Subtraction")
print(first_matrix - second_matrix)

##\nTask 8 — Matrix Multiplication

print("\nTask 8")

matrix_a = np.array([[1,2], [3,4]])
matrix_b = np.array([[5,6], [7,8]])

# matrix multiplication
print("Matrix Multiplication")
print(np.dot(matrix_a, matrix_b))

# transpose
print("Transpose")
print(matrix_a.T)
print("Neural networks use matrix multiplication for calculations.")

#Task 9 — Random Arrays

print("\nTask 9")

# random integer array
random_numbers = np.random.randint(1,100,(4,4))

print(random_numbers)

# random decimal values
random_decimal = np.random.rand(3,3)

print(random_decimal)

# maximum
print("Maximum value:", random_numbers.max())

# minimum
print("Minimum value:", random_numbers.min())

# average
print("Average value:", random_numbers.mean())
print("Random numbers help in AI training and testing.")

##Task 10 — Student Marks Analysis

print("\nTask 10")

student_marks = np.array([45,67,89,90,76,55,82,39,95,60])

# average marks
print("Average marks:", student_marks.mean())

# highest marks
print("Highest marks:", student_marks.max())

# lowest marks
print("Lowest marks:", student_marks.min())

# above 80
print("Students above 80")
print(student_marks[student_marks > 80])

# failed students
print("Failed students")
print(student_marks[student_marks < 50])



# # Task 11 — Image Pixel Simulation

print("\nTask 11")

# image pixels
pixel_data = np.random.randint(0,255,(5,5))

print(pixel_data)

# brightest pixel
print("Brightest pixel:", pixel_data.max())

# darkest pixel
print("Darkest pixel:", pixel_data.min())

# image shape
print("Shape:", pixel_data.shape)
print("AI reads images using arrays of pixels.")



##Task 12 — Data Normalization
print("\nTask 12")

normal_data = np.array([10,20,30,40,50])

# normalization
final_data = (normal_data - normal_data.min()) / (normal_data.max() - normal_data.min())

print(final_data)
print("Normalization improves AI model performance.")


##Task 13 — Mini AI Dataset \nTask

print("\nMINI AI  DATASET")

# dataset
ai_data = np.array([
    [20,25000,0],
    [25,40000,1],
    [30,50000,1],
    [22,20000,0],
    [28,45000,1]
])

print(ai_data)

# input features
input_data = ai_data[:,0:2]

# output labels
output_data = ai_data[:,2]

print("Input Features")
print(input_data)

print("Output Labels")
print(output_data)

# average salary
print("Average Salary:", input_data[:,1].mean())

# highest age
print("Highest Age:", input_data[:,0].max())

# dataset shape
print("Dataset Shape:", ai_data.shape)
