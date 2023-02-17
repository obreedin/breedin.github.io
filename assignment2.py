#receive input and store input as x
x = input()

#create empty string variable named z
z = ""

#make the letter y in variable x uppercase
for y in x:
	y = y.upper()
	#add y to z
	z += y

#print the newly created variable
print(z)