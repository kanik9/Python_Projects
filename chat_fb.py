import fbchat
from getpass import getpass
# if it must be in python 3 than use it .Otherwise don't
username = str(input("Username: "))
client = fbchat.Client(username, getpass())
no_of_friends = int(input("Number of friends: "))
for i in range(no_of_friends):
    name = str(input("Name: "))
    friends = client.getUsers(name)  # return a list of names
    friend = friends[0]
    msg = str(input("Message: "))
    sent = client.send(friend.uid, msg)
    if sent:
        print("Message sent successfully!")
