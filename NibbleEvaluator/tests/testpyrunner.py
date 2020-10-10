import sys
sys.path.append("..")
import unittest
import main
import os
from domain.code_test_status import TestStatus
from domain.runners.pyrunner import PyRunner


class Test0(unittest.TestCase):


    def test_with_two_inputs(self):

        path_evaluated_file = "G:\\TestFiles\\pysum.py"
        path_inputs_file = "G:\\TestFiles\\pysumInputs.txt"
        path_expected_output = "G:\\TestFiles\\pysumOutputs.txt"

        expected_test_output = TestStatus.TEST_PASSED

        real_test_output = main.test_file("python",path_evaluated_file,path_inputs_file,path_expected_output)

        self.assertEqual(expected_test_output,real_test_output)


    def test_py_one_to_five(self):
        path_evaluated_file = "G:\\TestFiles\\pyonetofive.py"
        path_inputs_file = None
        path_expected_output = "G:\\TestFiles\\pyonetofiveOutputs.txt"

        expected_test_output = TestStatus.TEST_PASSED

        real_test_output = main.test_file("python",path_evaluated_file,path_inputs_file,path_expected_output)

        self.assertEqual(expected_test_output,real_test_output)

    pass

    def test_py_while(self):

        path_evaluated_file = "G:\\TestFiles\\PyWhile.py"
        path_inputs_file = "G:\\TestFiles\\Inputs.txt"
        path_expected_output = "G:\\TestFiles\\Outputs.txt"

        expected_test_output = TestStatus.TEST_PASSED

        real_test_output = main.test_file("python",path_evaluated_file,path_inputs_file,path_expected_output)

        self.assertEqual(expected_test_output,real_test_output)

    def test_py_fail(self):

        path_evaluated_file = "G:\\TestFiles\\PyFail.py"
        path_inputs_file = "G:\\TestFiles\\Inputs.txt"
        path_expected_output = "G:\\TestFiles\\Outputs.txt"

        expected_test_output = TestStatus.EXECUTION_ERROR

        real_test_output = main.test_file("python",path_evaluated_file,path_inputs_file,path_expected_output)

        self.assertEqual(expected_test_output,real_test_output)


unittest.main()
