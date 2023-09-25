alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# def encrypt(text, shift):
#     output = ''
#     for letter in text:
#         index = alphabet.index(letter)
#         new_position = index+shift
#         new_text = alphabet[new_position]
#         output += new_text
#     print(output)
#
#
# def decrypt(text, shift):
#     output = ''
#     for letter in text:
#         index = alphabet.index(letter)
#         new_position = index-shift
#         new_text = alphabet[new_position]
#         output += new_text
#     print(output)

# define caesar function
def caesar(cipher_direction, text, shift):
    output = ''
    if cipher_direction == 'decode':
        shift *= -1

    for character in text:
        if character in alphabet:
            index = alphabet.index(character)
            new_position = index + shift
            output += alphabet[new_position]
        elif character in numbers:
            index = numbers.index(character)
            new_position = index + shift
            output += numbers[new_position]
        else:
            output += character

    print(output)

# rerun code using while loop
restart = True
while restart:
    direction = input("Type 'encode' to encrypt,\ntype 'decode' to decrypt:\n")
    user_text = input("Type your message:\n").lower()
    user_shift = int(input("Type the shift number:\n"))

    if user_shift > 26:
        user_shift %= 26

    caesar(cipher_direction=direction, text=user_text, shift=user_shift)
    user_choice_restart = input('Type "yes" to rerun "no" to stop:\n')
    if user_choice_restart == 'no':
        print('Goodbye')
        restart = False
