函数`input()`让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中。

函数input()接受一个参数：即要向用户显示的提示或说明。有时候，提示可能超过一行，在这种情况下，可将提示存储在一个变量中，再将该变量传递给函数input()。如下：
```py
prompt = "If you tell us who you are, we can presonalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
"""
If you tell us who you are, we can presonalize the messages you see.
What is your first name? hao

Hello, hao!
"""
```
