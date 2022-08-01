# 函数

## 定义函数
使用def关键字告诉Python你要定义一个函数，函数名后的括号内指明需要一些什么样的参数，最后，以冒号结尾。紧跟在冒号后的所有缩进行构成了函数体。
### 向函数传递信息
如下：
```py
def greet_user(usrname):
    """显示简单的问候语"""
    print("Hello, " + usrname.title() + "!")

greet_user('jesse')
```
在定义函数greet_user()时，变量usrname是一个形参，而传入的'jesse'是实参
## 传递实参
鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。向函数传递实参的方式有很多，可使用位置实参，这要求实参的顺序与形参的顺序相同；也可以使用关键字实参，其中每个实参都由变量名和值组成；还可以使用列表和字典。
如下：
```py
def describle_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#位置实参(注意传入参数的顺序与函数定义的顺序相同)
describe_pet('hamster', 'harry')

#关键字实参
describle_pet(animal_type='hamster', pet_name='harry')
```

### 默认值
编写函数时，可为每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用指定的实参值；否则，将使用形参的默认值。使用默认值可简化函数调用，还可清楚地指出函数的典型用法。

>注意：在使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参，这样能使Python依然能够正确解读位置实参。

当提供的实参多于或者少于函数完成其工作所需的信息时，将出现实参不匹配的错误。

## 返回值
函数可以处理一些数据，并返回一个或一组值。在函数中，可以使用return语句将值返回到调用函数的代码行。
### 返回简单值
```py
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# 调用返回值的函数时，需要提供一个变量，用于存储返回的值
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```
### 让实参变成可选的
有时候，需要让实参变成可选的，这样使用函数的人就只需在必要时才提供额外的信息。可使用默认值来让实参变成可选的。对于可选实参，可以使用空字符串为其赋予默认值，并将其移到形参列表的末尾，并在函数体中对于可选实参进行判断。如下：
```py
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    # 当middle_name为空字符串时，Python将其解读为False，非空时解读为True
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)
```
### 返回字典
函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。如下：
```py
def build_person(fisrt_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': fisrt_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
```
### 结合使用函数和while循环
```py
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("\n(enter 'q' at any time to quit)")
    
    f_name = input("first_name: ")
    if f_name == 'q':
        break

    l_name = input("last_name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
```
## 传递列表
如下：
```py
def greet_users(names):
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```
### 在函数中修改列表
将列表传递给函数后，函数就可以对其进行修改，在函数中对这个列表所做的修改都是永久性的，这能让你高效地处理大量的数据。
```py
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```
>Python3 中有六个标准的数据类型:<br/>
Number（数字）<br/>
String（字符串）<br/>
List（列表）<br/>
Tuple（元组）<br/>
Set（集合）<br/>
Dictionary（字典）<br/>
其中：<br/>
<font color=red>不可变数据</font>（3 个）：<br/>
Number（数字）<br/>
String（字符串）<br/>
Tuple（元组）<br/>
<font color=blue>可变数据</font>（3 个）：<br/>
List（列表）<br/>
Dictionary（字典）<br/>
Set（集合）<br/>
当需要在函数内修改参数而参数类型又是不可变数据类型时，可以使用可变数据类型来代替，这样就可以实现函数内修改参数。例，使用Dictionary（字典）数据类型来代替Number（数字）,String（字符串）,Tuple（元组）三种不可变数据类型。

### 禁止函数修改列表
有时候，需要禁止函数修改列表。此时，需向函数传递的参数不再为列表本身，而是列表的一个副本。即使用列表的一个切片。即：`print_models(unprinted_designs[:], completed_models)`

## 传递任意数量的实参
Python允许函数从调用语句中收集任意数量的实参。
如下：
```py
def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'greeb peppers', 'extra cheese')
```
形参名*toppings中的星号让Python创建一个名为topping的空元组，并将收到的所有值都封装到这个元组中。
### 结合使用位置实参和任意数量实参
如果要让函数接收不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
### 使用任意数量的关键字实参
有时，需要接受任意数量的实参，但是预先不知道传递给函数的会是什么样的信息。在这种情况下，可将函数编写成能接受任意数量的键值对。此时，使用双星号的形参会让Python创建一个空字典，并将收到的所有名称-值对都封装到这个字典中。例子如下：
```py
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)
# 输出为：{'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}
```
## 将函数存储在模块中
将函数储存在模块中，再将模块导入主程序，可以使主程序更容易理解。import语句允许在当前运行的程序文件中使用模块中的代码。

### 导入整个模块
要让函数是可导入的，得先创建模块。模块是扩展名为.py的文件，包含要导入到程序中的代码。对于`module_name.py`的文件使用`import module_name`即可将整个模块导入，并且可以使用`module_name.function_name`的结构来访问其中的函数。
如下：
```py
"""
# pizza.py
def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) + 
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
"""
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```
### 导入特定的函数
导入的语法为：
`from module_name import function_name`
且可以通过逗号分隔函数名，可根据需要从模块中导入任意数量的函数:
`from module_name import function_0, function_1, function_2`<br/>
若使用这种语法，调用函数时就无需使用句点。由于我们在import语句中显式地导入了函数，因此调用时只需指定其名称。
### 使用as给函数指定别名
如果导入的函数与程序中现有的名称冲突，或者函数的名称太长，可指定简短且独一无二的别名。要给函数指定这种别名，需要在导入时就这样做。<br/>
具体使用格式为：`from module_name import function_name as function_extraname`
### 使用as给模块指定别名
使用方法与上节类似：`import module_name as module_extraname`
### 导入模块中的所有函数
使用星号(*)运算符可以导入模块中的所有函数：`from module_name import *`<br/>
因为导入了所有的函数而不仅仅是模块，因此在导入后可以直接通过名称来调用每个函数，而不必使用句号表示法。但是在编写大型模块时，最好不要使用这样的导入方式，因为很有可能存在重名的函数。
<br/>
## 函数编写指南
+ 应给函数指定描述性名称，且只在其中使用小写字母和下划线，给模块命名时也应遵循上述约定。
+ 每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串的形式
+ 给形参指定默认值时，等号两边不要有空格。对于函数调用中的关键字实参，也应遵循这种约定
+ 如果形参很多，导致函数定义的长度超过了79字符，可在函数定义中输入左括号后按回车键，并在下一行按两次tab键，从而将形参列表和只缩进一层的函数体区分开，且后续参数列表行其缩进程度与你给第一个参数列表行指定的缩进程度相同
+ 应使用两个空行将相邻的函数分开
+ 所有的import语句都应尽量放在文件开头