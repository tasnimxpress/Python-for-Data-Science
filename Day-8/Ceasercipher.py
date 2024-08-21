alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Create a function called 'encrypt' and 'decrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(messege, key):
    encrypted_text = []
    # cipher_text = ""

    for i in messege:
        position = alphabet.index(i) + key
        char = alphabet[position]
        encrypted_text.append(char)
        # cipher_text += char

    print(f"The encoded text is: {"".join(encrypted_text)}")
    # print(f"The encoded text is: {cipher_text}")


def decrypt(chipher_text, key):
    decrypted_text = []

    for i in chipher_text:
        position = alphabet.index(i) - key
        char = alphabet[position]
        decrypted_text.append(char)

    print(f"The encoded text is: {"".join(decrypted_text)}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()
shift_amount = int(input("Type the shift number:\n"))

# cipher_work_done = True

# while not cipher_work_done:
if direction == 'encode':
    encrypt(text, shift_amount)
elif direction == 'decode':
    decrypt(text, shift_amount)
else:
    print('Please give a direction.')

    # cipher_again = input('Do you want to chiper again? Y for Yes, N for No: ')

    # if cipher_again == 'N':
    #     cipher_work_done = True
