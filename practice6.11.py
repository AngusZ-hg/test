cities = {
    'beijing':{'country':'china', 'population':'20 million', 'fact':'the capital of china'},
    'new york':{'country':'america', 'population':'20 million', 'fact':'a city in america'},
    'shanghai':{'country':'china', 'population':'20 million', 'fact':'a city in china'},
}

for city, informations in cities.items():
    print(city + ' is ' + informations['fact'])