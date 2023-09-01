
import unittest
import unittest.mock
import datetime
import statistics

import functions


# python -m unittest tests/test_functions.py

class TestClassForFunctions(unittest.TestCase):

    def test_arythmetic_mean(self):
        test_list = [1, 2, 3, 4, 5]
        aryth_mean = int(statistics.mean(test_list))       
        self.assertEqual(aryth_mean, functions.arythmetic_mean(test_list))

    def test_delet_val_from_list(self):
        test_list = [1, 2, 3, 1, 1, 4, 5, 1, 1]
        new_test_list = [2, 3, 4, 5]        
        self.assertEqual(new_test_list, functions.delet_val_from_list(test_list, 1)) 

    @unittest.mock.patch('functions.send_email')
    def test_create_user(self, mocked_send_mail):
        first_name = "Oleg"
        last_name = "Shcherbatiuk"
        birth_day = datetime.date(1981, 10, 11)
        address = "oleg.shcherbatiouk@gmail.com"
        functions.create_user(first_name, last_name, birth_day, address)

        address = "oleg.shcherbatiouk@gmail.com"
        message = "Testing Unittest!!! New user registered!!!"
        mocked_send_mail.assert_called_once_with(address, message)

    @unittest.mock.patch('functions.send_email')
    def test_send_eamil(self, mocked_send_mail):
        address = "oleg.shcherbatiouk@gmail.com"
        message = "Testing Unittest!!! New user registered!!!"
        functions.send_email(address, message)
        mocked_send_mail.assert_called_once_with(address, message)
