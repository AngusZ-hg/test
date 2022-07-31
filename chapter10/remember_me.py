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