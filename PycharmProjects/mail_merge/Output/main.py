#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"
names = []
with open("../Input/Names/invited_names.txt")as file:
    names = file.readlines()
for name in names:
    with open("../Input/Letters/starting_letter.docx") as file:
        letter_content = file.read()
        new_letter = letter_content.replace(PLACEHOLDER, name.strip())
    with open(f"../Output/ReadyToSend/letter({names.index(name)}).txt", mode='x') as file:
        file.write(new_letter)


