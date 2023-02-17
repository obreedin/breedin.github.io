#this assignment takes user input in the form of a base 10 number, 
#offers options from other base systems,
#and converts the user's number to those systems

def num_convert():
    #ask user for input in the form of a base 10 number
    base10input = int(input("Please enter a whole number:"))

    #offer the user options from other base systems
    b10input_b2 = bin(base10input)
    print(base10input, "converted to base 2, aka binary, is:", b10input_b2)

    #convert input into an octal (base 8) number
    b10input_b8 = oct(base10input)
    print(base10input, "converted to base 8, aka octal, is:", b10input_b8)

    #convert input into a hexadecimal
    b10input_hex = hex(base10input)
    print(base10input, "converted to hexadecimal is:", b10input_hex)


#boilerplate
if __name__ == "__main__":
    exit()

