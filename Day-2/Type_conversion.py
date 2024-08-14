"len function returns number of characters."

name = input("What is your name?\n")
num_char = len(name)

"However, len doesn't like working with integeres."

# print("Your name has" + num_char + "characters.") :error

"So, Heres come type conversion."

string_num_char = str(num_char)

print("Your name has" + " " + string_num_char + " " + "characters.")
