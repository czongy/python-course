#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_temp = letter.read()
    for name in name_list:
        name_stripped = name.strip()
        insert_name = letter_temp.replace("[name]", name_stripped)
        with open(f"./Output/ReadyToSend/{name_stripped}.txt", "w") as named_letter:
            named_letter.write(insert_name)
