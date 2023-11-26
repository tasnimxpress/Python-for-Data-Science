number = [1, 2, 3]
new_number = [n+1 for n in number]
print(new_number)

my_name = 'Tasnim'
new_name = [letter for letter in my_name]
print(new_name)

new_list = range(1, 5)
comprehension = [n*2 for n in new_list]
print(comprehension)


names = ['Tasnim', 'kona', 'tupai', 'kutush', 'jannatul', 'rumpa', 'ferdous']
cap_name = [item.upper() for item in names if len(item) > 5]
print(cap_name)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
new_squared = []
for n in numbers:
    new_n = n**2
    new_squared.append(new_n)
print(new_squared)

squared_number = [item**2 for item in numbers]
print(squared_number)

