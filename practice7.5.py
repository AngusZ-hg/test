prompt = "Please tell me your age."
prompt += "\nEnter 'quit' to quit.\n"

total_price = 0
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age <= 3 and age >= 0:
        total_price += 0
    elif age > 3 and age <=12:
        total_price += 10
    elif age > 12:
        total_price += 15
    else:
        print("Please enter a right age, thanks.")
print("the total price is " + str(total_price) + '.')