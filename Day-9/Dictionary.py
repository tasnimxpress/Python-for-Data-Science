# Dictionary

# creating dictionary
programming_dictionary = {
    'Bug': 'Error in a code that prevent code to run as expected.',
    'Loop': 'A loop is a sequence of instruction s that is continually repeated until a certain condition is reached.',

}
print(programming_dictionary)

# add key: value
programming_dictionary['Recursion'] = 'Recursion is a programming concept in which a function, class method, or routine invokes itself to re-apply an algorithm on a different set of inputs.'
print(programming_dictionary)

# Retreve a value
print(programming_dictionary['Bug'])  # print only value

# loop through dictionary
for key in programming_dictionary:
    print(key)  # print all the key
    print(programming_dictionary[key])  # print key and value

# empty dictionary
empty_dict = {}
print(empty_dict)
