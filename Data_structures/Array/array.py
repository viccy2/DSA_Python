# basic /dynamic /one dimensional array
array = [1, 5, 7, 9, 2, 4]


# array transversal
def transverse_array():
    for i in range(len(array)):
        print(array[i])


# array insertion
def add(data1, data2):
    array.insert(data1, data2)
    print(array)


# array deletion
def remove(data):
    if data in array:
        array.remove(data)
        print(array)
    else:
        print(data, "not in array")


# array searching
def find_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# find min of array
def min_array(arr):
    a = sorted(arr)
    print(a[0])

# find max of array
def max_array(arr):
    a = sorted(arr)
    print(a[-1])


 min_array(array)

