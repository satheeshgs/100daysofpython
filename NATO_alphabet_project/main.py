import pandas as pd
nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

#Loop through rows of a data frame
#for (index, row) in nato_df.iterrows():
    #Access index and row
    #Access row.student or row.score
#    print(row.code)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows() }
print(nato_dict)

#2. Create a list of the phonetic code words from a word that the user inputs.
encoded_list = []
while len(encoded_list) == 0:
    word = input("Please enter the word you want to encode: \n")
    try:
        encoded_list = [nato_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry only letters in the dictionary please!")
    else:
        print(encoded_list)

