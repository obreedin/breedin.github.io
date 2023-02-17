#experiment with strings

my_word = "new,1"

#length of the world
len(my_word)

print(my_word)

type(print) 

my_word.split()
my_word.rstrip()
my_word.strip()
my_word.isalpha()
my_word.capitalize()
my_word.upper()


my_string = "helko world"
print(my_string)
print(my_string[3])

my_string[3] = "l"

my_string = "hello world"

#creates a string defining an object
word = "word"

#defining object c as 0
c = 0

#for loop, for everything in that word going through one at a time, for every element in the sequence do something
#"for" is usualy in purple, meaning it is built in ... "flow control"

for character in word:
  c += 1
  print(character + chr)

#type error because you are trying to add a character to a string
# bad snippet! why?
# how can we fix it
# note: end:+prt

sentence = "I love programming."

#split the sentence
#split() function splits a string into a list
sentence.split('love')

S = sentence.split()
print(S)
S.split(',')

for word in S.split(','):
    pass

#casing
S.upper()

#length
len(S)


