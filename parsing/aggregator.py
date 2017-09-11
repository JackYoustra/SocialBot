from parsing import  fb_parser, hangouts_parser, skype_parser
from parsing.user import User
import os
import pickle

serialization_path = "serialized_data.bin"

target_user_list = []

def make_aggregate():
    aggregate = fb_parser.target_user_list +  hangouts_parser.target_user_list + skype_parser.target_user_list
    for user in aggregate:
        if user.name == "Jack":
            print("Jack: " + str(len(user.messageList)))

        i = 0
        merged = False
        while i < len(target_user_list):
            current = target_user_list[i]
            if current.name.lower() in user.name.lower() or user.name.lower() in current.name.lower():
                target_user_list.remove(current)
                target_user_list.append(User(current.name, user.messageList + current.messageList))
                merged = True
                break
            i += 1

        if not merged:
            target_user_list.append(user)

serialization = True
if serialization:
    try:
        with open(serialization_path, "rb") as binary:
            target_user_list = pickle.load(binary)
        print("preloaded")

    except Exception:
        make_aggregate()
        with open(serialization_path, "wb") as binary:
            pickle.dump(target_user_list, binary)
else:
    make_aggregate()

print(len(target_user_list))