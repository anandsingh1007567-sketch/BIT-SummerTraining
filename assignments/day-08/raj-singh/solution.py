import numpy as np
### Question 1: Create a NumPy Array
marks=np.array([85, 90, 78, 92, 88])
print(marks)


### Question 2: Array Shape and Size
shape=np.shape(marks)
size=np.size(marks)
print("Shape:", shape)
print("Size:", size)


### Question 3: Basic Calculations
total=np.sum(marks)
average=np.mean(marks)
max=np.max(marks)
min=np.min(marks)
print("Total:", total)
print("Average:", average)
print("Maximum:", max)
print("Minimum:", min)


### Question 4: Create a 2D Array
arr_2d=np.array([[10, 20, 30],
 [40, 50, 60]])
print(arr_2d)



### Question 5: Indexing and Slicing
print(arr_2d[1,1])
print(arr_2d[0])


### Question 6: Element-Wise Operations
numbers = np.array([1, 2, 3, 4, 5])
print(numbers*10)



## Question 7: Filter Values
new_arr=marks[marks>=90]
print(new_arr)


### Question 8: Student Marks Matrix
column = [ "Python", "Data Analytics", "AI marks" ]
ave_arr=np.array([])
mark=np.array([[85, 78, 90],
               [92, 88, 95],
               [76, 82, 80]])
for i in range(len(mark)):
    average=np.mean(mark[i])
    ave_arr=np.append(ave_arr,average)
print(np.round(ave_arr,2))