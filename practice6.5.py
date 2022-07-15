rivers = {
    'nile':'egypt',
    'changjiang':'china',
    'huanghe':'china',
}
for river,nation in rivers.items():
    print('the '+ river + ' runs through ' + nation + '.')
for river in rivers.keys():
    print(river, end = ' ')
print('')
for nation in set(rivers.values()):
    print(nation, end = ' ')