prompt = "Please input a number: "

temp_num = input(prompt)
digit = int(temp_num)
if digit % 2 == 0:
    print("This is a even number.")
else:
    print("This is an odd number.")