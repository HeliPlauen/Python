
# 

from collections import namedtuple


user = {
    "name": "barracuda2000",
    "status": "unlocked"
}


class BannedException(Exception):
    ...


def banned_user_bad_implementation(user:dict):
    try:
        set_banned_status(user)
    except:
        raise  BannedException(f"The user with username {user['name']} was not banned!!!")


def banned_user_good_implementation(user:dict):
    try:
        set_banned_status(user)
    except Exception as err:
        raise  BannedException(f"The user with username {user['name']} was not banned!!!") from err


def set_banned_status(user):
    aaaa['status'] = "banned"


if __name__ == "__main__":
    print("-------------------------------------------------------------------------------------------")
    #banned_user_bad_implementation(user)
    print("-------------------------------------------------------------------------------------------")
    banned_user_good_implementation(user)
    print("-------------------------------------------------------------------------------------------")
