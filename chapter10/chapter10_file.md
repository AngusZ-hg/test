# 文件和异常
## 从文件中读取数据
要使用文本文件中的信息，首先需要将信息读取到内存中。为此，可以一次性读取文件中的全部内容，也可以以每次一行的方式逐步读取。
### 读取整个文件
要读取文件，我们先创建一个包含几行文本的文件。如文件夹中的pi_digits.txt文件。使用如下代码读取并打印出其内容：
```py
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip())
```
在这个程序中，第1行代码做了大量的工作。
要以任何方式使用文件，都需要先打开文件，这样才能访问它。函数open()接受一个参数：要打开的文件的名称。Python将在当前执行的文件所在目录查找指定的文件。函数open()返回一个表示文件的对象，Python将这个对象存储在我们将在后面使用的变量中。<br/>
关键字with在不再需要访问文件后将其关闭。也可以通过调用open()和close()来打开和关闭文件，但这样做时，如果程序存在bug，导致close()语句未执行，文件将不会关闭。使用关键字with可以让Python自己在合适的时机自动将其关闭。<br/>
在有了文件对象后，我们使用方法read()读取这个文件的全部内容，并将其作为一个字符串存储在变量contents中。当文件末尾有空字符串时，read()会原封不动读取空字符串。如果想删除末尾的空行，可以在print语句中使用rstrip()。

### 文件路径
根据你组织文件的形式，有时可能要打开不在程序文件所属目录中的文件。要让Python打开不与程序文件位于同一个目录中的文件，需要提供文件路径。<br/>
可以使用相对文件路径来打开该文件夹中的文件。相对文件路径和Python到指定的位置去查找，而该位置是相对于当前运行的程序所在目录的。在Linux和OS X中，可以使用如下代码：
`with open('text_files/filename.txt') as file_object:`
而在windows系统中，文件路径应使用反斜杠( \\ )而不是斜杠( / )
`with open('text_files\filename.txt') as file_object:`<br/>
你还可以将文件在计算机中的准确位置告诉Python，这样就不用关系当前运行的程序存储在什么地方了，这称为绝对文件路径。在相对路径行不通时，可以使用绝对路径。为明确指出你希望Python到哪里去找，你需要提供完整的路径。<br/>
绝对路径通常比相对路径更长，因此将其存储在一个变量中，再将该变量传递给open()会有所帮助。在Linux和OS X中，绝对路径类似下面这样：
```py
file_path = '/home/other_files/text_files/filename.txt'
with open(file_path) as file_object:
```
而在Windows系统中，类似下面这样：
```py
file_path = 'C:\Users\other_files\text_files\filename.txt'
with open(file_path) as file_object:
```
通过使用绝对路径，可读取系统任何地方的文件。
>由于反斜杠在Python中被视为转义标记，为在Windows中确保万无一失，应以原始字符串的方式指定路径，即在开头的单引号前加上r。

### 逐行读取
要以每次一行的方式检查文件，可对文件对象使用for循环：
```py
filename = r'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
```
当使用上述代码时，会发现每次输出的后面都会存在一个空白行。在这个文件中，每行的末尾都有一个看不见的换行符，而print语句也会加上一个换行符。仍然可以使用rstrip()来消除这些空白行。
```py
filename = r'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
    file_object.seek(0)
    for line in file_object:
        print(line.rstrip())
```
>文件是流；从文件读取或写入文件会将文件指针推进到新位置。遍历文件以逐行读取也不例外。一旦您读取了文件中的所有行，文件位置将一直保留在最后，并且再次迭代不会产生任何额外信息。需要使用以下命令将文件读取位置倒file.seek()回到开头。

### 创建一个一个包含文件各行内容的列表
使用关键字with时，open()返回的文件对象只在with代码块内可用。如果要在with代码块外面访问文件的内容，可在with代码块内将文件的各行存储在一个列表中，并在with代码块外使用该列表。
方法readlines()从文件中读取每一行，将其存储在一个列表中并返回。
```py
filename = r'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
```
### 使用文件的内容
```py
filename = r'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
```
在变量pi_string存储的字符串中，包含位于每行左边的空格，为删除这些空格，可以使用strip()而不是rstrip()。
>在读取文本文件时，Python将其中所有的文本都解读为字符串。如果读取的是数字，需要使用函数int()或者函数float()将其转化为数值使用。

>可使用方法replace()将字符串中的特定单词都替换为另一个单词。如下：
```py
>>>message = "I really like dogs."
>>>message.replace('dog', 'cat')
'I really like cats.'
```
## 写入文件
### 写入空文件
要将文本写入文件，你在调用open()时需要提供另一个实参，告诉Python你要写入打开的文件。
```py
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
```
在这个示例中，调用open()时提供了两个实参。第一个实参时要打开的文件的名称，第二个实参('w')告诉Python，我们要以写入模式打开这个文件。打开文件时，可指定读取模式('r')，写入模式('w')，附加模式('a')或让你能够读取和写入文件的模式('r+')。如果你省略了模式实参，Python将以默认的只读模式打开文件。
如果你要写入的文件不存在，函数open()将自动创建它。然而，以写入('w')模式打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件。
>Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。

### 写入多行
函数write()不会在你写入的文本末尾添加换行符，因此为了让每个字符串都单独占一行，需要在write()语句中包含换行符。

### 附加到文件
如果要给文件添加内容而不是覆盖原有内容，可使用附加模式打开文件。当以附加模式打开文件时，Python不会在返回文件对象前清空文件，而你写入到文件的行都将添加到文件末尾。如果指定的文件不存在，Python将为你创建一个空文件。

## 异常
Python使用被称为异常的特殊对象来管理程序执行期间发生的错误。每当发生让Python不知所措的错误时，它都会创建一个异常对象。如果你编写了处理该异常的代码，程序将继续运行；如果你未对异常进行处理，程序将停止，并显示一个traceback，其中包含有关异常的报告。
异常是使用try-except代码块处理的。try-except代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办。使用了try-except代码块时，即便出现异常，程序也将继续运行：显示你编写的友好的错误消息，而不是令用户迷惑的traceback。

### 处理ZeroDivisionError异常
当将一个数字除以0时，traceback会指出一个ZeroDivisionError异常对象。

### 使用try-except代码块
当你认为可能发生了错误时，可编写一个try-except代码块来处理可能引发的异常。
处理ZeroDivisionError异常的try-except代码块类似于下面这样：
```py
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```
我们将导致错误的代码行妨碍了一个try代码块中。如果try中的代码运行起来没有问题，Python将跳过except代码块，否则将查找这样的except代码块，并运行其中的代码，即其中指定的错误与引发的错误相同。
如果try-except代码块后面还有代码块，程序将接着运行，因为已经告诉了Python如何处理这种错误。
### 使用异常避免崩溃
发生错误时，如果程序还有工作没有完成，妥善地处理错误就尤为重要。这种情况经常会现在要求用户提供输入的程序中；如果程序能够妥善地处理无效输入，就能再提示用户提供有效输入，而不至于崩溃。
### else代码块
通过将可能引发错误的代码放在try-except代码块中，可提高这个程序抵御错误的能力。错误是执行除法运算的代码导致的，因此我们需要将它放在try-except代码块中。这个示例还包含一个else代码块；依赖于try代码块成功执行的代码都应放到else代码块中：
```py
print("Give me two numbers,  and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Second number can't be zero.")
    else:
        print(answer)
```
except代码块告诉Python，出现某种异常时应该怎么办。如果try代码块因该种错误而失败，我们就打印一条友好的消息。
<br/>
try-except-else代码块的工作原理如下：Python尝试执行try代码块中的代码；只有可能引发异常的代码才需要放在try语句中。一些仅在try代码块成功执行时才需要运行的代码需要放到else代码块中。except代码块告诉Python，如果它尝试运行try代码块中的代码时引发了指定的异常时该怎么办。

### 处理FileNotFoundError异常
使用文件时，一种常见的问题是找不到文件：要查找的文件可能在其他地方、文件名可能不正确或者这个文件根本就不存在。对于这些情形，都可以用try-except代码块处理。

### 分析文本
可以使用方法split()来分析字符串中有多少单词。方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储在一个列表中，我们可以通过一个变量接收这个列表并对其进行一系列的分析。

### 失败时一声不吭
Python有一个pass语句，可在代码块中使用它来让Python什么都不要做。pass语句还充当了占位符，它提醒你在程序的这个地方什么都没有做，并且以后也许要在这里做些什么。

## 存储数据
很多程序都要求用户输入某种信息，用户关闭程序时，你几乎总是要保存他们提供的信息；一种简单的方式是使用模块json来存储数据。
模块json让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。你还可以使用json在Python程序之间分享数据。更重要的是，JSON数据格式并非是Python专用的，这让你能够将以JSON格式存储的数据与使用其他编程语言的人分享。
>JSON（JavaScript Object Notation）格式最初是为JavaScript开发的，但随后形成了一种常见格式。

### 使用json.dump()和json.load()
我们来编写一个存储一组数字的简短程序，再编写一个将这些数字读取到内存中的程序。第一个程序将使用json.dump()来存储这组数字，而第二个程序将使用json.load()。
函数json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象。
```py
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
```
我们先导入模块json，再创建一个数字列表。我们指定了要将该数字列表要存储的文件的名称。通常使用文件扩展名.json来指出文件存储的数据为JSON格式。接下来，我们以写入模式打开这个文件，让json能够将数据写入其中。我们使用json.dump()将数字列表存储到文件number.json中。
下面的程序使用json.load()将这个列表读取到内存中：
```py
import json

filename = 'number.json'

with open(filename, 'r') as f_obj:
    numbers = json.load(f_obj)

print(numbers)
```
这次我们以读取方式打开这个文件，我们使用函数json.load()加载存储在numbers.json中的信息，并将其存储在变量numbers中。
### 保存和读取用户生成的数据
对于用户生成的数据，使用json保存它们大有用处，因为这些数据将在程序停止运行时丢失。
```py
import json

filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What's your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
```

### 重构
将代码划分成一系列完成具体工作的函数，这样的过程称为重构。重构让代码更清晰、更易于理解、更容易扩展。对于上一节编写的代码，我们将其重构如下：
```py
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
```