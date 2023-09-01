
import datetime

import functions


class User:
    def __init__(self, first_name, last_name, birthday_date, address):
        self.__first_name = first_name
        self.__last_name = last_name
        birthday_date_list = birthday_date.strip().split(",")
        if len(birthday_date_list) != 3:
            raise ValueError
        self.__birthday = datetime.date(
            int(birthday_date_list[0]), 
            int(birthday_date_list[1]), 
            int(birthday_date_list[2])
        )
        self.__email = address

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_birthday(self):
        return self.__birthday

    def get_email(self):
        return self.__email

    def get_full_name(self):
        return "{} {}".format(self.__last_name, self.__first_name)

    def get_short_name(self):
        first_name = self.__first_name
        return "{} {}.".format(self.__last_name, first_name[0])

    def get_age(self):
        birthday = self.__birthday
        current_date = datetime.datetime.now()
        return current_date.year - birthday.year

    def __str__(self):
        return f"{self.get_full_name()}, {self.get_age()} years."

    def register_new_user(self):
        new_user = functions.send_email(            
            self.__email,
            "Testing Unittest!!! Congratulations!!! You successfully registered!!!"
        )        

    def find_user_in_database(self):
        pass

