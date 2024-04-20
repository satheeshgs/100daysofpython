#don't worry about closing file with the with keyword
#with open("text_file.txt") as file:
#    contents = file.read()
#    print(contents)

#writing to a file
with open("text_file.txt", mode="w") as file:
    file.write("\nnew_text")

#write mode creates a new file and writes if the file does not exist