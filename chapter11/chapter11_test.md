# 测试代码
## 单元测试和测试用例
Python标准库中的模块unittest提供了代码测试工具。单元测试用于核实函数的某个方面没有问题；测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求。良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情形的测试。全覆盖式测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。
### 可通过的测试
创建测试用例的语法需要一段时间才能习惯。但测试用例创建后，再添加针对函数的单元测试就很简单了。要为函数编写测试用例，可先导入模块unittest以及要测试的函数，再创建一个继承unittest.TestCase的类，并编写一系列方法对函数行为的不同方面进行测试。
下面是一个只包含一个方法的测试用例，它检查函数get_formatted_name()在给定名和姓时能否正确地工作：
```py
## test_name_function.py

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
        self.assertEqual(formatted_name, 'Janis Joplin')  # 1

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
首先，我们导入了模块unittest和要测试的函数get_formatted_name()。我们创建一个名为NameTestCase的类，用于包含一系列针对get_formatted_name()的单元测试。这个类必须继承unittest.TestCase类，这样Python才知道如何运行你编写的测试。
NameTestCase只包含一个方法，用于测试get_formatted_name()的一个方面。我们将这个方法命名为test_first_last_name()，因为我们要核实的是只有名和姓的姓名能否被正确地格式化。我们运行test_name_function.py时，所有以test_打头的方法都将自动运行。
在1处，我们使用了unittest类最有用的功能之一：一个<font color=green>断言</font>方法。断言方法用来核实得到的结果是否与期望的结果一致。
在这里，我们知道get_formatted_name()应返回这样的姓名，即名和姓的首字母为大写，且它们之间有一个空格，因此我们期望formatted_name的值为Janis Joplin。为检查是否如此，我们调用unittest的方法assertEqual()，并向它传递formatted_name和'Janis Joplin'。代码行self.assertEqual(formatted_name, 'Janis Joplin')的意思是说：“将formatted_name与'Janis Joplin'相比较，如果它们相等，就万事大吉，如果它们不相等，跟我说一声！”
运行结果如下：
```py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
第一行的句点表明有一个测试通过了。接下来的一行指出Python运行了一个测试，消耗的时间不到0.001秒。最后的OK表示该测试用例中的所有单元测试都通过了。
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
### 不能通过的用例
我们来修改get_formatted_name()，使其能够处理中间名，但这样做时，故意让这个函数无法处理只有名和姓的姓名。此时运行结果如下：
```py
## name_function.py
"""
def get_formatted_name(first, middle, last):
    """生成整洁的姓名"""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()
"""
E
======================================================================
ERROR: test_first_last_name (__main__.NameTestCase)
能够正确地处理
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\hao zhang\Desktop\test\chapter11\test_name_function.py", line 15, in test_first_last_name
    formatted_name = get_formatted_name('janis', 'joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```
其中包含的信息很多，因为测试未通过时，需要让你知道的事情可能有很多。第一行输出只有一个字母E，它指出测试用例有一个单元测试导致了错误。接下来，我们看到NameTestCase中的test_first_last_name()导致了错误。测试用例包含众多单元的测试时，知道哪个测试未通过至关重要。之后我们看到了一个标准的traceback，它指出函数调用get_formatted_name('janis', 'joplin')有问题，因为它缺少一个必不可少的位置实参。
我们还看到运行了一个单元测试。最后，还看到一条消息，它指出整个测试用例都未通过，因为运行该测试用例时发生了一个错误。
### 测试未通过时怎么办
测试未通过时怎么办？如果你检查的条件没错，测试通过了意味着函数的行为是对的。而测试未通过意味着你编写的新代码有错。因此，测试未通过时，不要修改测试，而应修复导致测试不能通过的代码：检查刚对函数所做的修改，找出导致函数行为不符合预期的修改。
### 添加新测试
确定get_formatted_name()又能正确地处理简单的姓名后，我们再编写一个测试，用于测试包含中间名的姓名。为此，我们在NamesTestCase类中再添加一个方法：
```py
import unittest
#import sys
#sys.path.append('..')
#from chapter10.remember_me import get_stored_username
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """能够正确地处理像Wolffang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
```
运行结果如下：
```py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
>所有的单测文件名都需要满足test_.py格式或_test.py格式。
在单测文件中，测试类以Test开头，并且不能带有 init 方法(注意：定义class时，需要以T开头，不然pytest是不会去运行该class的)
在单测类中，可以包含一个或多个test_开头的函数。
此时会自动从当前目录及子目录中寻找符合上述约束的测试函数来执行。
## 测试类
前面我们编写了针对了单个函数的测试，下面来编写针对类的测试。很多程序中都会用到类，因此能够证明你的类能够正确地工作会大有裨益。如果针对类的测试通过了，你就能确信对类所做的改进没有意外地破坏其原有的行为。
### 各种断言方法
Python在unittest.TestCase类中提供了很多断言方法。断言方法检查你认为应该满足的条件是否确实满足。如果条件确实满足，你对程序行为的假设就得到了确认，你就可以确信其中没有错误。如果你认为应该满足的条件实际上并不满足，Python将引发异常。
下表列出了6个常用的断言方法。使用这些方法可核实返回的值等于或不等于预期的值、返回的值为True或False、返回的值在列表中或不在列表中。你只能在继承unittest.TestCase的类中使用这些方法。
|方法|用途|
|-|-|
|assertEqual(a, b)|核实a == b|
|assertNotEqual(a, b)|核实a != b|
|assertTrue(x)|核实x为True|
|assertFalse(x)|核实x为False|
|assertIn(item, list)|核实item在list中|
|assertNotIn(item, list)|核实item不在list中|
### 一个要测试的类
类的测试与函数的测试类似——你所做的大部分工作都是测试类中方法的行为，但存在一些不同之处，下面来编写一个类进行测试。来看一个帮助管理匿名调查的类：
```py
## survey.py
class AnonymousSurvey():
    """收集匿名调查问卷的答案"""

    def __init__(self,question):
        self.question = question
        self.responses = []
    
    def show_question(self):
        print(self.question)
    
    def store_response(self, new_response):
        self.responses.append(new_response)
    
    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
```
这个类首先存储了一个你指定的调查问题，并创建了一个空列表，用于存储答案。这个类包含打印问题的方法、在答案列表中添加新答案的方法以及将存储在列表中的答案都打印出来的方法。要创建这个类的实例，只需提供一个问题即可。
为证明这个类能正确地工作，我们编写如下的程序来使用它：
```py
## language_survey.py

from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn and speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    else:
        my_survey.store_response(response)

# 显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
```
如果我们想让每个用户都可输入多个答案；且只列出不同的答案，并指出每个答案出现了多少次；再编写一个类，用于管理非匿名调查。
进行上述修改存在风险，可能会影响AnonymousSurvey类的当前行为。例如，允许每位用户输入多个答案时，可能不小心修改了处理单个答案的方式。要确认在开发这个模块时没有破坏既有行为，可以编写针对这个类的测试。
### 测试AnonymousSurvey类
下面来编写一个测试，对AnonymousSurvey类的行为的一个方面进行验证：如果用户面对调查问题时只提供了一个答案，这个答案也能被妥善地存储。为此，我们将在这个答案被存储后，使用方法assertIn()来核实它包含在答案列表中：
```py
## test_survey.py

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def test_score_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)
    
unittest.main()
```
我们首先导入了模块unittest以及要测试的类AnonymousSurvey。我们将测试用例命名为TestAnonymousSurvey，它也继承了unittest.TestCase。第一个测试方法验证调查问题的单个答案被存储后，会包含在调查结果列表中。对于这个方法，一个不错的描述性名称是test_store_single_response()。如果测试未通过，我们就能通过输出中的方法名得知，在存储调查答案方面存在问题。
要测试类的行为，需要创建其实例。我们使用问题"What language did you first learn to speak?"创建了一个名为my_survey的实例，然后使用方法store_response()存储了单个答案English。当我们运行test_survey.py时，测试结果如下：
```py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
下面来核实用户提供三个答案时，它们也将被妥善地存储。为此，我们在TestAnonymousSurvey中再添加一个test_store_three_responses()方法：
```py
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def test_score_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)
    
    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(responses, my_survey.responses)
    
unittest.main()
```
运行结果如下：
```py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
做法的效果很好，但是测试有一些重复的地方，下面使用unittest的另一项功能来提高它们的效率。
### 方法setUp()
之前我们在每个测试方法中都创建了一个AnonymousSurvey实例，并在每个方法中都创建了答案。unittest.TestCase类包含方法setUp()，让我们只需创建这些对象依次，并在每个测试方法中使用它们。如果你在TestCase类中包含了方法setUp(),Python将先运行它，再运行各个以test_打头的方法。这样，在你编写的每个测试方法中都可使用方法setUp()中创建的对象了。
下面使用setUp()来创建一个调查对象和一组答案，供方法test_store_single_response()和test_store_three_responses()使用：
```py
## test_setUp.py
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_score_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn('English', self.my_survey.responses)
    
    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
    
unittest.main()
```
运行结果如下：
```py
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```
方法setUp()做了两件事情，创建一个调查对象，创建一个答案列表。存储在这两样东西的变量名包含前缀self，因此可在这个类的任何地方使用。
测试自己编写的类时，方法setUp()让测试方法编写起来更容易：可在setUp()中创建一系列实例并设置它们的属性，再在测试方法中直接使用这些实例。
>运行测试用例时，每完成一个单元测试，Python都将打印一个字符：测试通过时打印一个句点；测试引发错误时打印一个E；测试导致断言失败时打印一个F。这就是你运行测试用例时，在输出的第一行看到的句点和字符数量各不相同的原因。如果测试用例包含很多单元测试，需要运行很长时间，就可以通过观察这些结果来获悉有多少个测试通过了。