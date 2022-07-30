def city_country(city_name, country_name):
    temp = '"' + city_name.title() + ', ' + country_name.title() + '"'
    return temp

city = city_country('Shanghai', 'china')
print(city)

city = city_country('beijing', country_name='china')
print(city)

city = city_country('new york', 'america')
print(city)

def make_album(singer_name, album_name, number=''):
    album = {'singer_name': singer_name, 'album_name': album_name}
    if number:
        album['song_number'] = number
    return album

my_album = make_album('jay chou', number=7, album_name='qilixiang')
print(my_album)