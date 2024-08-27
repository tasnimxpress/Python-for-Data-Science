# ############ DEBUGGING#####################

# # Describe Problem
# from random import randint


# def my_function():
#     for i in range(1, 20):  # it never reaches to 20
#         if i == 20:
#             print("You got it")


# my_function()

# # Reproduce the Bug
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# # 6 is causing the bug - it is out of range; we need 0-5 range instead
# print(dice_imgs[6])


# # Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)  # this line should be indented
#     print(b_list)


# mutate([1, 2, 3, 5, 8, 13])

# # Even or Odd
# number = int(input('Number:'))
# if number % 2 = 0:  # it should be ==
#     print('Even')
# else:
#     print('Odd')

# # fizzbuzz
# target = int(input('Number: '))

# for number in range(1, target + 1):
#     if number % 3 == 0 or number % 5 == 0:  # need and not or
#         print('Fizzbuzz')
#     if number % 3 == 0:  # need elif not if
#         print('Fizz')
#     if number % 5 == 0:  # need elif not if
#         print('Buzz')
#     else:
#         print(f'{number}')
