"This program will take a number for range, and add all the even number between 0 and the input number."

Range = int(input('Enter the number: '))

total = 0
if Range > 1000:
    print('Enter a value less than 1000, for speed issue.')
else:
    for n in range(1, Range + 1):
        if n % 2 == 0:
            print(n)
            total += n

    print(total)
