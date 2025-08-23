# Taking in users' favourite restaurant and number
# and printing them out.
string_fav = input("What is your favourite restaurant? ")
int_fav = int(input("What is your favourite number? "))
print(string_fav)
print(int_fav)
# A ValueError occurs because the string_fav variable is a string that 
# consists of text and cannot be converted to an integer. It is an 
# invalid type for conversion.
print(int(string_fav))
