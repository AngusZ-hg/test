names = ['jen','sarah','edward','phil','angus','edmonton','luyao']
favorate_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name in names:
    if name in favorate_languages.keys():
        print(name+ ', thanks')
    else:
        print(name+ ', welcome')