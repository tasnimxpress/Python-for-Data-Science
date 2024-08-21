alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Create a function called 'encrypt' and 'decrypt' that takes the 'text' and 'shift' as inputs.


def cipher_machine(cipher_direction, messege, key):
    end_text = []
    # cipher_text = ""

    for i in messege:
        if i in alphabet:
            if cipher_direction == 'encode':
                position = alphabet.index(i) + key
                char = alphabet[position]
            elif cipher_direction == 'decode':
                position = alphabet.index(i) - key
                char = alphabet[position]
            else:
                print('Direction is required.')
        else:
            char = i

        end_text.append(char)
        # cipher_text += char

    print(f"The encoded text is: {"".join(end_text)}")
    # print(f"The encoded text is: {cipher_text}")


cipher_work_done = False

while not cipher_work_done:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))

    cipher_machine(direction, text, shift_amount)

    cipher_again = input(
        "Type 'Y' if you want to cipher again? Otherwise type 'N' for No: ").lower()
    if cipher_again == 'n':
        cipher_work_done = True
        print('Goodbye!')
