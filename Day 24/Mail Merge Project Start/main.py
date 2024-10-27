#TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
    # print(content)
with open("./Input/Names/invited_names.txt") as i_names:
    names = i_names.readlines()
    # print(names)

for name in names:
    new_name = name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode = "w") as final_letter:
        final_letter.write(content.replace("[name]", new_name))


#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp