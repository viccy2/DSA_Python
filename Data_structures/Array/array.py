# basic /dynamic /one dimensional array
array = [1, 2, 3, 4, 5]
print(array)

# fixed size array
fixed_array = [0] * 5
print(fixed_array)

# array transversal
for i in range(len(array)):
    print(array[i]),
    end = ""

# array insertion
a = 10
b = 2
array.insert(b, a)
print(array)

# array deletion
c = 6
if c in array:
    array.remove(c)
else:
    print(c, 'not in array')
print(array)


# array searching
def find_element(element):
    for i in range(len(array)):
        if array[i] == element:
            print('found')
        else:
            print("element not found")


find_element(1)
