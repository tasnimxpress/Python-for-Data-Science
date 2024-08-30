"This program take a group of peoples height as input and calculate the average"

heights = input('Enter heights: ').split()

for i in range(0, len(heights)):
    heights[i] = int(heights[i])

average_heights = round(sum(heights)/len(heights), 2)
num_people = len(heights)
total_height = sum(heights)

print(f'Total height: {total_height}')
print(f'Number of people: {num_people}')
print(f'Average heights: {average_heights}')


"Alternative approach"
print('\nResult from alternative approach.\n')

total_sum = 0
for i in heights:
    total_sum += i

number_people = 0
for n in heights:
    number_people += 1

average = round(total_sum/num_people, 2)

print(f'Total height: {total_sum}')
print(f'Number of people: {number_people}')
print(f'Average height: {average}')
