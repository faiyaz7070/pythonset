# 2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
#     - *Input*: None
#     - *Output*: "Type of variable1: <class 'int'>, value: 10..."

# integer
i = 5
print("Type of integer: " + str(type(i)) + ", value: " + str(i))

# float
f = 5.5
print("Type of float: " + str(type(f)) + ", value: "+ str(f))

#string
s = "Hello, world!"
print("Type of string: " + str(type(s)) + ", value: "+ str(s))

# boolean
b = True
print("Type of boolean: " + str(type(b)) + ", value: "+ str(b))

# list
l = [1,2,3,4]
print("Type of list: " + str(type(l)) + ", value: "+ str(l))

# tuple
t = (1,2,3,4)
print("Type of tuple: " + str(type(t)) + ", value: "+ str(t))

# dictionary (object in javascript)
d = {
    "name":"aman kumar",
    "student_code":"fw21_0675"
}
print("Type of dictionary: " + str(type(d)) + ", value: "+ str(d))

# set 
set1 = {2, 3, 4}
set2 = {4, 5, 6}

union_set = set1.union(set2)   
intersection_set = set1.intersection(set2)
difference_set = set1 - set2

print("Type of union_set: " + str(type(union_set)) + ", value: "+ str(union_set))
print("Type of intersection_set: " + str(type(intersection_set)) + ", value: "+ str(intersection_set))
print("Type of difference_set: " + str(type(difference_set)) + ", value: "+ str(difference_set))