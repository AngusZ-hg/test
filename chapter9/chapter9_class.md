# 类
## 创建和使用类
根据约定，在Python中，首字母大写的名称指的是类。类定义中的括号代表继承自哪个超类，当括号为空时，表示从空白创建这个类，此时创建的类为基类。
```py
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        print(self.name.title() + "rolled over!")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

my_dog.sit()
my_dog.roll_over()
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
```
### 方法__init__()

类中的函数称为方法。有关函数的一切都适用于方法，就目前而言，唯一重要的差别是调用方法的方式。\_\_init__()是一个特殊的方法，每当根据类创建新的实例时，Python都会自动运行它。在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。
我们将方法__init__()定义成了包含三个形参：self、name和age。在这个方法的定义中，形参self必不可少，还必须位于其他形参的前面。

>为何必须在方法定义中包含形参self呢？
Python调用__init__()方法创建类的实例时，将自动传入实参self。每个与类相关联的方法调用都自动传入实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。我们创建实例时，Python将调用类的方法__init__()。我们将通过实参向类传递参数时，self会自动传递。
以self为前缀的变量都可供类中的所有方法使用，我们还可以通过类在任何实例来访问这些变量。如`self.name = name`获取存储在形参name中的值，并将其存储到变量name中，然后该变量被关联到当前创建的实例。像这样可通过实例访问的变量称为**属性**。

### 根据类创建实例
创建实例需要根据__init__()的形参列表传入实参，其中self由Python自动调用，因此只需传入除开self外的参数。
*命名约定：通常可以认为首字母大写的名称指的是类，而小写的名称指的是根据类创建的实例。*
#### 访问属性
要访问实例的属性，可使用句号表示法。如`my_dog.name`
#### 调用方法
要调用方法，可指定实例的名称和要调用的方法，并用句点分隔它们。如`my_dog.sit()`

## 使用类和实例
类编写好后，大部分时间都将花在使用根据类创建的实例上。你需要执行的一个重要任务时修改实例的属性。你可以直接修改实例的属性，也可以编写方法以特定的方式进行修改。
### 给属性指定默认值
类中的每个属性都必须具有初始值，哪怕这个值是0或空字符串。在有些情况下，如设置默认值时，在方法__init__()内指定这种初始值是可行的；如果你对某个属性这样做了，就无需包含为它提供初始值的形参。
### 修改属性的值
可以通过三种不同的方式修改属性的值：直接通过实例进行修改；通过方法进行设置；通过方法进行递增（增加特定的值）。
#### 直接修改属性的值
通过实例直接访问属性的值并修改它。如：`my_car.odometer_reading = 23`
#### 通过方法修改属性的值
无需直接访问属性，而可将值传递给一个方法，由它在内部进行更新。这种方式需要在类的内部定义一个修改属性值的方法。如：`my_car.update_odometer(23)`
#### 通过方法对属性值进行递增
有时需要将属性值递增特定的量，而不是将其设置为全新的值。其实现取决于类中修改值的方法。

## 继承
编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用继承。一个类继承另一个类时，它将自动获得另一个类的所有属性和方法：原有的类称为父类，或者说是超类，而新类称为子类。子类继承了父类的所有属性和方法。同时还可以定义自己的属性和方法。
### 子类的方法__init__()
创建子类的实例时，Python首先需要完成的任务是给父类的所有属性赋值。为此，子类的方法__init__()需要父类施以援手。
如下：
```py
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    --snip--

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.describe_battery()
```
创建子类时，父类必须包含在当前文件中，且位于子类前面。定义子类时，必须在括号内指定父类的名称。方法__init__()接受创建Car实例所需的信息。
super()是一个特殊函数，帮助Python将父类和子类关联起来。这行代码让Python调用父类的方法__init__()，让子类实例包含父类的所有属性。
### 给子类定义属性和方法
让一个类继承另一个类后，可添加区分子类和父类所需的新属性和方法。如上面例子的battery_size属性和describe_battery方法。
### 重写父类的方法
对于父类的方法，只要它不符合子类模拟的实物的行为，都可以对其进行重写。为此，可在子类中定义一个这样的方法，即它与要重写的父类方法同名。这样，Python将不会考虑这个父类方法，而只关注你在子类定义中定义的相应方法。即对于子类和父类同名的方法，Python将忽略父类的方法，而运行子类中重写的同名方法。
### 将实例用作属性
属性和方法清单可能会越创建越多，这种情况下，可能需要将类的一部分作为一个独立的提取出来。
```py
class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
        pass

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # 1

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()  # 2
```
我们定义了一个名为Battery的新类，同时在1处，，我们添加了一个self.battery的属性，这行代码让Python创建一个新的Battery()实例，并将该实例存储在属性self.battery中。同时在2处，Python将在实例my_tesla中查找属性battery，并对存储在该属性中的Battery实例调用方法describe_battery()。

## 导入类
随着不断给类添加功能，文件可能变得很长，即便你妥善使用了继承也会如此。Python允许将类存储在模块中，然后在主程序中导入所需的模块。
### 导入单个类
你应该为自己创建的每个模块都编写文档字符串。而导入类是一种有效的编程方式。从module_name.py中导入class_name,导入语法如下：
`from module_name import class_name`
### 在一个模块中导入多个类
同一个模块中可以存储任意数量的类，但是原则上同一个模块中的类应该存在某种关联性。导入多个类时，使用逗号分隔各个类。对于从module_name.py中导入多个class_name，语法如下：
`from module_name import class1_name, class2_name`
### 导入模块中的所有类
与导入所有函数相同。当导入module_name.py中所有的类时，语法格式如下：
`from module_name import *`
不推荐使用这种导入方式。

## 类编码风格
**类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。实例名和模块名都采用小写格式，并在单词之间加上下划线**。
对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时才哟个的格式约定。每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。
可使用空行来组织代码，但不要滥用。**在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类**。
需要同时导入标准库中的模块和你编写的模块时，**先编写导入标准库模块的import语句，再添加一个空行，然后编写导入你编写的模块的import语句**。在包含多条import语句的程序中，这种做法让人更容易明白程序使用的各个模块都来自何方。