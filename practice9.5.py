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

user1 = User('hao', 'zhang', location='qichun')
user2 = User('juntao', 'zhang', location='guanyao', age=13)
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

for number in range(1,10):
    user1.increment_login_attempts()
    print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)
