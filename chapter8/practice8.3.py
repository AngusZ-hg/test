def make_shirt(size, sample='I love Python'):
    print("The size of the T-shirt is " + size +", and the sample is " + sample + ".")

def describe_city(city_name, country='China'):
    print(city_name.title() + " is in " + country.title())

make_shirt('L')
make_shirt("M", 'Born to be different')
describe_city('beijing')
describe_city('shanghai')
describe_city('new york', 'america')