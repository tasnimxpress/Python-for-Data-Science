# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open('E:/GitHub/100DaysOfPython/Day-24/Input/Names/invited_names.txt', 'r') as file:
    nameList = list(file.readlines())
    # print(type(nameList[0]))

    with open('E:/GitHub/100DaysOfPython/Day-24/Input/Letters/starting_letter.txt', 'r') as sampleLetter:
        SLetter = sampleLetter.read()
        for name in nameList:
            readyLetter = SLetter.replace(
                '[name]', name.strip())
            print(readyLetter)

            with open(f'E:/GitHub/100DaysOfPython/Day-24/Output/ReadyToSend/LetterFor_{name.strip()}.txt', 'w') as completedLetter:
                completedLetter.write(readyLetter)
