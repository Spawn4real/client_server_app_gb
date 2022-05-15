"""Unit-тесты клиента"""

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import create_presense, procces_ans


class TestClass(unittest.TestCase):
    """Класс с тестами"""

    def test_presense(self):
        """Тест коректности запроса"""
        test = create_presense()
        test[TIME] = 1.1
        self.assertEqual(test, {
            ACTION: PRESENCE,
            TIME: 1.1,
            USER: {
                ACCOUNT_NAME: 'Guest'
                }
            })

    def test_200(self):
        """Тест корректности разбора ответа 200"""
        self.assertEqual(procces_ans({RESPONSE: 200}), '200 : OK')

    def test_400(self):
        """Тест корректности разбора 400"""
        self.assertEqual(procces_ans({RESPONSE: 400, ERROR: 'BAD REQUEST'}), '400 : BAD REQUEST')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, procces_ans, {ERROR: 'BAD REQUEST'})


if __name__ == '__main__':
    unittest.main()