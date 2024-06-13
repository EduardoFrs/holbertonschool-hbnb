import json

def save_user(user_object):
    # takes a user object and converts it to a dict
    # unset=true avoids including attributes with default value
    # creates then the users.json

    user_data = user_object.dict(exclude_unset=True)
    with open('users.json', 'w') as outfile:
        json.dump(user_data,outfile)

