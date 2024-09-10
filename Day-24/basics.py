# read the file mode='r'
with open('E:/GitHub/100DaysOfPython/Day-24/file.txt', 'r') as file:
    print(file.read())


# overwrite the file mode='w'
with open('E:/GitHub/100DaysOfPython/Day-24/file.txt', 'w') as file:
    file.write('\nthis is new text')

# write to the file without deleting the previous text : mode='a'
with open('E:/GitHub/100DaysOfPython/Day-24/file.txt', 'a') as file:
    s = file.write('\nThis is text without deleting first text')
    print(type(file))
