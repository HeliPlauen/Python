
from userclass import User


# "Oleg" "Shcherbatiuk" "1981, 10, 11"
# "oleg.shcherbatiouk@gmail.com"

def create_user():

    # Get data from user
    user_data = {}
    user_data["first_name"] = input("Input your first name: ")
    user_data["last_name"] = input("Input your last name: ")
    user_data["birthday_date"] = input("Input your birtday date (year, month, day): ")
    user_data["address"] = input("Input your e-mail please: ")

    # Create new user object
    T1 = User(user_data["first_name"], user_data["last_name"], 
                 user_data["birthday_date"], user_data["address"])
    print(T1.get_first_name())
    print(T1.get_last_name())
    print(T1.get_birthday())
    print(T1.get_full_name())
    print(T1.get_short_name())
    print(T1.get_age())
    print(T1.__str__())
    T1.register_new_user()
 

if __name__ == "__main__":
    try:
        create_user()
    except Exception as err:
        print(f"Error: {err}!!!")
