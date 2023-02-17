my_observations = {"dogs":0, "cats":2}
my_query = "dogs"
my_value = my_observations[my_query]
print(my_value)

my_observations = {"dogs" : 0, "cats" : 2}
print(my_observations["dogs"])

my_dict = {} # dictionary
my_dict = dict() # dictionary
my_dict = {0} # NOT a dictionary -- what type is this? -- integer?
my_dict = {"key": "value"} # dictionary
print(my_dict)

my_observations["ducks"] = 1
my_observations["ducks"] += 1

if "ducks" in my_observations:
    print("theres a duck!")
else:
    print("theres no ducks!")

my_observations["ducks"] = "ducks are cute"

print(my_observations["ducks"])

print(my_dict["geese"])