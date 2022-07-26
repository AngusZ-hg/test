#8.12
def sandwichs_list(*materials):
    print("\nThere are ",end='')
    for number in range(0, len(materials)):
        if number ==len(materials)-1:
            print(materials[number], end='')
        else:
            print(materials[number], end=', ')
    print(" in your sandwich!")

sandwichs_list('onion', 'potato', 'meat')
sandwichs_list('meat', 'vegetable', 'tomato')
sandwichs_list('fish', 'tomato', 'onion')

#8.13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('hao', 'zhang',
                            location='wuhan',
                            field='cs',
                            age=25)
print(user_profile)

#8.14
def make_car(manufacturer, band, **car_info):
    car_profile = {}
    car_profile['Band'] = band
    car_profile['Manufacturer'] = manufacturer
    for key,value in car_info.items():
        car_profile[key] = value
    return car_profile

car = make_car('subaru', 'outbank', color='blue', tow_package=True)
print(car)