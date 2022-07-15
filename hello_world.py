numbers = list(range(1,10))
for number in numbers:
    print(number,end=' ')
print('\n')
for number in numbers:
    if number == 1:
        print(number,'st')
    elif number == 2:
        print(number,'nd')
    elif number == 3:
        print(number,'rd')
    elif number >= 4 and number <= 9:
        print(number,'th')