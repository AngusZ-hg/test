# 字典
## 使用字典
字典是一系列键-值对。可以使用键来访问与之对应相关联的值，值可以是数字、字符串、列表乃至字典，事实上，任何Python对象都可以作为字典中的值。

在Python中，字典用放在花括号{ }的一系列键-值对表示，如：
`alien_0 = {'color':'green', 'point':5}`
指定键时，Python将返回与之相关联的值。键和值之间用冒号分隔，而键-值对之间用逗号分隔。在字典中，键-值对没有存储上限。
### 访问字典中的值
要获取与键相关联的值，可依次指定字典名和放在方括号内的键，这将返回字典中与键相关联的值。如：
```py
alien_0 = {'color':'green', 'point':5}
new_points = alien_0['point']
print('You just earned '+str(new_points)+' points!')
"""
You just earned 5 points!
"""
```
### 添加键-值对
字典是一种动态结构，可以随时添加键-值对。要添加键-值对，可依次指定字典名、用方括号括起来的键和相关联的值。
```py
alien_0 = {'color':'green', 'point':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
"""
{'color': 'green', 'point': 5}
{'color': 'green', 'point': 5, 'x_position': 0, 'y_position': 25}
"""
```
### 修改字典中的值
要修改字典中的值，可依次指定字典名、用方括号括起来的键以及与该键相关联的新值。如：
`alien_0['color'] = 'yellow'`
### 删除键-值对
可以使用del语句将相应的键-值对彻底删除。使用del语句时，必须指定字典名和要删除的键。如：
`del alien_0['point']`
- - -
## 遍历字典
### 遍历键-值对
要编写用于遍历字典的for循环，可声明两个变量，用于存储键-值对中的键和值，对于这两个变量，可以使用任何名称，如：
```py
for key,value in user_0.items()
```
for语句的第二部分包含字典名和方法`items()`,它返回一个键-值对列表。
注意：Python不关心键-值对的存储顺序，只跟踪键和值之间的关联关系。
### 遍历字典中的所有键
在不需要使用字典中的值时，方法`key()`很有用。如：
```py
for key in user_0.keys()
```
遍历字典时会默认遍历所有的键，因此将上述for循环可改为`for key in user_0`，输出将不变。

另可使用当前键来访问与之相关联的值，如下：
```py
favorate_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}
friends = ['phil','sarah']
for name in favorate_languages:
	print(name.title())
	if name in friends:
		print('Hi ' + name.title() + ', I see your favorate language is '+ favorate_languages[name].title() + '!')
```
方法`keys()`返回一个列表，其中包含字典中的所有键。
### 按顺序遍历字典中的所有键
字典总是明确地记录键和值之间的关联关系，但是在获取字典中的元素时，获取顺序是不可预测的。要以特定的顺序返回元素，一种办法是在for循环中对返回的键进行排序，可以使用函数`sorted()`来获得特定顺序排列的键列表的副本。如：
```py
for name in sorted(favorate_languages.keys())
```
### 遍历字典中的所有值
使用方法`values()`，它返回一个值列表，而不包含任何键。使用方式与`keys()`类似，`values()`返回的列表不考虑是否重复，如果要剔除重复项，可以使用集合`set()`。如：
```py
for language in set(favorate_languages.values())
```
- - -
## 嵌套
将一些列字典存储在列表中，或将列表作为值存储在字典中，称为嵌套。
### 字典列表
如下：
```py
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
"""
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
"""
```
### 在字典中存储列表
每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。
如下：
```py
favorate_languages = {
    'jen':['python', 'ruby'],
    'sarah':['c'],
    'edward':['ruby', 'go'],
    'phil':['python', 'haskell'],
}
for name, languages in favorate_languages.items():
    if len(languages) == 1:
        print('\n' + name + "'s favorate language is " + languages[0] + '.')
    else:
        print('\n' + name + "'s favorate languages are:")
        for language in languages:
            print('\t' + language)
"""

jen's favorate languages are:
        python
        ruby

sarah's favorate language is c.

edward's favorate languages are:
        ruby
        go

phil's favorate languages are:
        python
        haskell
"""
```
### 在字典中存储字典
字典可以作为值嵌套在另一个字典中。