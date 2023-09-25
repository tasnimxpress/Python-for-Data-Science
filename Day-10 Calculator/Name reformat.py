# this code will return titlecase full name

def format_name(first_name, last_name):
    name = first_name +' '+ last_name
    full_name = name.title()
    return full_name

user_first_name = input('first name: ')
user_last_name = input('last name: ')

user_name = format_name(user_first_name, user_last_name)
print(user_name)