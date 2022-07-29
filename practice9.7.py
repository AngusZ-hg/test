class User():
    def __init__(self, first_name, last_name, **distrib):
        self.profile = {}
        self.profile['first_name'] = first_name
        self.profile['last_name'] = last_name
        for key,value in distrib.items():
            self.profile[key] = value
        self.login_attempts = 0
        pass

    def describe_user(self):
        for key,value in self.profile.items():
            print(key + ': ' + str(value))
    
    def greet_user(self):
        print("Hello, " + self.profile['first_name'].title() + '!')
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):

    def __init__(self, first_name, last_name, **distrib):
        super().__init__(first_name, last_name, **distrib)
        self.privileges = Privileges()
    
my_admin = Admin('hao', 'zhang')
my_admin.privileges.show_privileges()
