import sys
import unittest
import nibble_evaluator
from domain.code_test_status import TestStatus

class Test1(unittest.TestCase):

    def test_1(self):
        path_evaluated_file = "C:\\Users\\Chelo\\Documents\\TestFiles\\HolaMundo.cpp"

        path_input = "Input"

        expected_output = "¡HOLA MUNDO!"

        expected_test_output = {'status': TestStatus.TEST_PASSED, 'percentaje' : 100.00}

        real_test_output = nibble_evaluator.test_file(path_evaluated_file,path_input,expected_output)

        self.assertEqual(expected_test_output,real_test_output)

    pass

unittest.main()
