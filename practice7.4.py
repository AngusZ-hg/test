prompt = "Please enter the material you want to add in pizza."
prompt += "\nEnter 'quit' to quit.\n"

message = True
while message:
    material = input(prompt)
    if material == 'quit':
        print('Thanks for your order.')
        message = False
    else:
        print('We will add ' + material + ' in your pizza.')
