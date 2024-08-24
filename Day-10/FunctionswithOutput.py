# Functions with output

def format_name(first_name, last_name):
    name = (first_name + " " + last_name).title()
    return name


f_name = input('First name: ')
l_name = input('Last name: ')

full_name = format_name(f_name, l_name)

print(full_name)
# print(format_name(f_name, l_name))
