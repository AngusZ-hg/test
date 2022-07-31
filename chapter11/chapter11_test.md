# 测试代码
## 单元测试和测试用例
Python标准库中的模块unittest提供了代码测试工具。单元测试用于核实函数的某个方面没有问题；测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求。良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情形的测试。全覆盖式测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。
### 可通过的测试
创建测试用例的语法需要一段时间才能习惯。但测试用例创建后，再添加针对函数的单元测试就很简单了。要为函数编写测试用例，可先导入模块unittest以及要测试的函数，再创建一个继承unittest.TestCase的类，并编写一系列方法对函数行为的不同方面进行测试。
下面是一个只包含一个方法的测试用例，它检查函数get_formatted_name()在给定名和姓时能否正确地工作：
```py
import unittest
# import sys
# sys.path.append('..')
# from chapter10.remember_me import get_stored_username
from name_function import get_formatted_name

# print(sys.path)

class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()

"""
import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    filename = 'username.json'
    username = input("What's your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username ==None:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()
"""
```
>在本示例中，name_function.py为当前路径下的模块，当使用上一级路径下的文件时，可以添加sys.path来导入，如示例中被注释掉的代码所示。但是需要注意的是，由于Python的特性，在导入中的函数时，会执行一遍导入模块中未缩进的代码，也就是上例中的greet_user()，这将导致不必要的输出。为了防止这种情况，可以使用__name__来避免。
\_\_name__:内置属性，记录一个字符串，如果是当前的执行程序，则__name__ = \_\_main__,如果是作为模块被其他程序导入，__name__则等于模块的路径名，对于本例，当在get_stored_name()中加入`print(__name__)`时，输出为`chapter10.remember_me`。所以，可以根据对__name__的判断实现import的模块不会执行直接执行的代码
```py
import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    print(__name__)
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    filename = 'username.json'
    username = input("What's your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username ==None:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

if __name__ =='__main__':
    greet_user()
```