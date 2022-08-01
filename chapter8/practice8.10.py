def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for number in range(0,len(magicians)):
        magicians[number] = 'The Great ' + magicians[number]

magicians = ['zhang hao', 'zhang juntao', 'zhang fan']
make_great(magicians)
show_magicians(magicians)