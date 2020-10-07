import sys
import unittest
import nibble_evaluator
from domain.code_test_status import TestStatus

class Test1(unittest.TestCase):

    def test_1(self):
        path_evaluated_file = "C:\\Users\\Chelo\\Documents\\TestFiles\\HolaMundo.cpp"

        path_input = "Input"

        path_expected_output = "C:\\Users\\Chelo\\Documents\\TestFiles\\Outputs.txt"

        expected_test_output = TestStatus.TEST_PASSED
        real_test_output = nibble_evaluator.test_file(path_evaluated_file,None,path_expected_output)

        print(real_test_output)
        self.assertEqual(expected_test_output,real_test_output)


    def test_multiple_outputs(self):

        path_evaluated_file = "C:\\Users\\Chelo\\Documents\\TestFiles\\HolaMundo2.cpp"
        path_expected_output = "C:\\Users\\Chelo\\Documents\\TestFiles\\HolaMundo2Outputs.txt"

        expected_test_output = TestStatus.TEST_PASSED
        real_test_output = nibble_evaluator.test_file(path_evaluated_file,None,path_expected_output)

        self.assertEqual(expected_test_output,real_test_output)


    def test_one_to_five(self):

        path_evaluated_file = "C:\\Users\\Chelo\\Documents\\TestFiles\\OneToFive.cpp"
        path_expected_output = "C:\\Users\\Chelo\\Documents\\TestFiles\\OneToFiveOutputs.txt"

        expected_test_output = TestStatus.TEST_PASSED

        real_test_output = nibble_evaluator.test_file(path_evaluated_file,None,path_expected_output)

        self.assertEqual(expected_test_output,real_test_output)

    pass

unittest.main()
