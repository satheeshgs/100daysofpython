#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#get invited names
with open("./Input/Names/invited_names.txt") as file:
    invited_names = file.read()

#get starting letter
with open("./Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

#split names by new line
names = str.split(invited_names, "\n")
#print(names)

#replace starting letter with name and write to files
for name in names:
    letter = starting_letter.replace("[name]", name)
    letter_name = "letter_for_" + name + ".txt"
    #print(letter, letter_name)
    with open(f"./Output/ReadyToSend/{letter_name}", mode='w') as file:
        file.write(letter)
