# creating class
class User:
    # initialize attributes
    # attributes that the object has - like characteristics
    def __init__(self, userid, username):
        self.id = userid
        self.name = username
        self.follower = 0  # set default value
        self.following = 0

    # creating method
    # method that a object does - how a object act
    # method is functions associated with object
    def follow(self, user):
        user.follower += 1
        self.following += 1


# creating object from class
Object_1 = User(1, 'user_1')

# creating attribute
# attribute is a variable associated with a object
Object_2 = User(2, 'user_2')

print(Object_1.id)
print(Object_2.name)

Object_1.follow(Object_2)

print(Object_2.follower)
print(Object_1.follower)
