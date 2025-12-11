# userid = 0
#
# class User:
#     def __init__(self):
#         global userid
#         print("new user being created")
#         userid += 1
#         print(f"User {userid} created.")
#
# while userid < 10:
#     user = User()
#
class User():
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        self.followers_list = []
        self.following_list = []

    def follow(self, user):
        user.followers +=1
        user.followers_list.append(self)
        self.following +=1
        self.following_list.append(user)

user_1 = User("001", "Angela")
user_2 = User("002", "Henrique")
user_3 = User("003", "Magnolia")
user_4 = User("004", "Dad")

user_1.follow(user_2)
user_4.follow(user_2)
user_2.follow(user_4)
user_3.follow(user_4)
user_3.follow(user_2)
print(f"{user_2.username} has {user_2.followers} followers.")

# person_list = []
# for follower in user_2.followers_list:
#     person_list.append(follower.username)
# print(f"They are, in chronological order, {", ".join(person_list)}.")
print(f"They are, in chronological order, {", ".join([follower.username for follower in user_2.followers_list])}.") #this line summarizes the last 4 into a list comprehension. 

#print(user_2.followers_list[0].username) #prints a specific follower username who started following you and became a hallmark, e.g., follower number 100.
