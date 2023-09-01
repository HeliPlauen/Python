
import unittest
import unittest.mock
import datetime

import userclass
import functions


# python -m unittest tests/test_classes.py
# "Oleg" "Shcherbatiuk" "1981, 10, 11"
# "oleg.shcherbatiouk@gmail.com"

class TestClassForClass(unittest.TestCase):
    
    def setUp(self):
        self.first_name = "Oleg"
        self.last_name = "Shcherbatiuk"
        self.birth_day = "1981, 10, 11"
        self.email = "oleg.shcherbatiouk@gmail.com"
        self.testclass = userclass.User(
            self.first_name, 
            self.last_name, 
            self.birth_day,
            self.email
        )
   
    def test_constructor(self):
        self.assertEqual(self.first_name, self.testclass.get_first_name())
        self.assertEqual(self.last_name, self.testclass.get_last_name())
        self.assertEqual(datetime.date(1981, 10, 11), self.testclass.get_birthday())
        self.assertEqual(self.email, self.testclass.get_email())  
        
    def test_get_full_name(self):
        full_name = f"{self.last_name} {self.first_name}"
        self.assertEqual(full_name, self.testclass.get_full_name())

    def test_short_name(self):
        short_name = f"{self.last_name} {self.first_name[0]}."
        self.assertEqual(short_name, self.testclass.get_short_name())

    def test_get_age(self):
        birthday = datetime.date(1981, 10, 11)
        current_date = datetime.datetime.now()
        age = current_date.year - birthday.year
        self.assertEqual(age, self.testclass.get_age())

    def test_str(self):
        current_str = f"{self.last_name} {self.first_name}, 42 years."
        self.assertEqual(current_str, self.testclass.__str__())

    @unittest.mock.patch('functions.send_email')
    def test_register_new_user(self, mocked_send_mail):
        self.testclass.register_new_user()
        mocked_send_mail.assert_called_once_with(
            self.email,
            "Testing Unittest!!! Congratulations!!! You successfully registered!!!"
        )
