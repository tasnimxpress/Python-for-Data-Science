# creating class
class User:
    # initialize attributes
    def __init__(self, userid, username):
        self.id = userid
        self.name = username
        self.follower = 0  # set default value

    pass


# creating object from class
Object_1 = User(1, 'user_1')

# creating attribute
# attribute is a variable associated with a object
Object_2 = User(2, 'user_2')

print(Object_1.id)
print(Object_2.name)
print(Object_1.follower)
