from mongoengine import *
from datetime import datetime
import os
import json

connect("New")


# Def Documents


class User(Document):
    username = StringField(unique=True, required=True)
    email = EmailField(unique=True)
    password = BinaryField(required=True)
    age = IntField()
    bio = StringField(max_length=150)
    categories = ListField()
    admin = BooleanField(default=False)
    registered = BooleanField(default=False)
    date_created = DateTimeField(default=datetime.utcnow)
    date_created = DateTimeField(default=datetime.utcnow)

    def json(self):
        user_dict = {
            "username": self.username,
            "email": self.email,
            "age": self.age,
            "bio": self.bio,
            "categories": self.categories,
            "registered": self.registered

        }
        return json.dumps(user_dict)

    meta = {
        "indexes": ["username", "email"],
        "ordering": ["-date_created"]}


user = User(
    username="Jaime Guerrero",
    email="jjguerrero032@gmail.com",
    password=os.urandom(16),
    age=17,
    bio="This is my first MongoDB Project",
    admin=True)
""" 
try:
    user.save()
except NotUniqueError:
    print("Username or email is not unique")
"""

# Queries
users = User.objects()
for user in users:
    print(user.username, user.email)

# Filtering
"""
admin_users = User.objects(admin=True)
for a in admin_users:
    print(a.username)
"""

# Attempt to find a user not made
try:
    Guillermo = User.objects(username="Guillermo").get()
except DoesNotExist:
    print("User Not Found")
