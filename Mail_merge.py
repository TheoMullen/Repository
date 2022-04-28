#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp




invited_names = "/Users/theo/Downloads/Mail Merge Project Start/Input/Names/invited_names.txt"

send_folder = "/Users/theo/Downloads/MailMergeProjectStart/Output/ReadyToSend"

starting_letter = "/Users/theo/Downloads/Mail Merge Project Start/Input/Letters/starting_letter.txt"



with open(invited_names) as names:
    for _ in names:
        name = _.strip()
        with open(starting_letter, mode='r') as template:
            lines = template.readlines()

        with open(f"./Output/ ReadyToSend/{name}'s letter", mode='w') as new_letter:
            for line in lines:
                adjusted_line = line.replace("[name]", name)
                new_letter.write(adjusted_line)









