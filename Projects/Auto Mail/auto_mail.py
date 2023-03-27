# read every name on the invitation_list as a new line
with open("./invitation_list.txt") as name_file:
    names = name_file.readlines()

# read the whole letter as a text string to replace specific context
placeholder = "[name]"
with open("./letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        name = name.rstrip()

        # create a variable to attach the modified string
        # use "r" mode because we do not want to change the original letter content
        new_letter = letter_content.replace(placeholder, name)

        # use the new_letter content and save to the "Output" folder
        # use "w" mode to create a new txt file for each person
        with open(f"./Output/letter_for_{name}.txt", mode="w") as completed_file:
            completed_file.write(new_letter)
