sandwich_orders = ['aa', 'pastrami', 'bb', 'pastrami', 'cc', 'dd', 'pastrami']
finished_sandwiches = []

print("Pastrami sandwich has sold out.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    temp_sandwich = sandwich_orders.pop()
    print("I made your " + temp_sandwich + " sandwich.")
    finished_sandwiches.append(temp_sandwich)
for sandwich in finished_sandwiches:
    print(sandwich)
