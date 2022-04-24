from user import User

user1 = User('talg', 'talgreen1@yahoo.com', '1234', 'qa automation')
user1.get_user_info()

print(user1.get_num_of_users())

user2 = User('talg', 'talgreen1@yahoo.com', '1234', 'qa automation')

print(User.get_num_of_users())