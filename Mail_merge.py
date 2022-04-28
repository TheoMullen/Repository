

invited_names = "./Mail Merge Project Start/Input/Names/invited_names.txt"

send_folder = "./MailMergeProjectStart/Output/ReadyToSend"

starting_letter = "./Mail Merge Project Start/Input/Letters/starting_letter.txt"




with open(invited_names) as names:
    for _ in names:
        name = _.strip()
        with open(starting_letter, mode='r') as template:
            lines = template.readlines()

        with open(f"./Output/ ReadyToSend/{name}'s letter", mode='w') as new_letter:
            for line in lines:
                adjusted_line = line.replace("[name]", name)
                new_letter.write(adjusted_line)









