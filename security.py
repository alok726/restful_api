from users import User


def authenticate(username, password):
    user = User.find_by_username(username)

    if user and user.password == password:
        return user


def identity(payload):
    user = User.find_by_id(payload['identity'])
    return user