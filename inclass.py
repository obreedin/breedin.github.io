counter = 0
number_of_Is=0
sentence_list = "This is a sentence".split("")
for word in sentence:
    counter += 1
    if word == "I":
        number_of_Is += 1


from datetime import datetime

startTime = datetime.now()
for _ in range ():

#code from 2 feb pad

#declaring a list

my_list_0 = list()
my_list_1 = []
my_list_2 = [0, 1, 3]

#can you predict the outcome of the following?
[0, 1, 2] + [4]
#it produces a list [0,1,2,4]

[0, 1, 2,] * 4
#it repeats the list 4 times

[0,1,2][1]
#idk what is happening here

[0, 1, 2][-1]
#or here

[0, 1, 2][4]
#error message: list index out of range

print(len([0, 1, 2]))
#prints the length of the list

print(len([0, 1, 2][-1]))
#error, object of type 'int' has no length

my_list = [0, 1, 2]
my_list.append(3)
my_list.append("hello")
print(my_list)
qm = my_list.pop(0)
print(my_list)
print(qm)

#experiment with slicing
#notation [b:e], beginning and end positions, includes the beginning, 
#but not end

my_list[:]
my_list[3:]
my_list[:-2]
my_list[::2]
print(my_list)

M = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
M

zero = 0
a = [zero]
b = [zero]
c = a[:]
a2 = a

hex(id(zero))
id(a)
id(b)
id(a2)

def add_two_numbers (n1, n2):
    return(n1 + n2)
c = add_two_numbers("name1" , "name2")
print(c)
