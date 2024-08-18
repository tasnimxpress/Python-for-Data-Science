"This program take a group of peoples height as input and calculate the average"

heights = input('Enter heights: ').split()

for i in range(0, len(heights)):
    heights[i] = int(heights[i])

average_heights = sum(heights)/len(heights)
print(f'Average heights: {average_heights}')


"Alternative approach"

total_sum = 0
for i in heights:
    total_sum += i

# print(total_sum)

average = total_sum/len(heights)
print(f'Average height: {average}')
