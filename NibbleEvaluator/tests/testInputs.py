import sys
sys.path.append("..")
import unittest
from app import nibble_evaluator
import os
from domain.code_test_status import TestStatus
from domain.runners.cpprunner import CppRunner

class Test0(unittest.TestCase):

    def test_with_two_inputs(self):

        path_evaluated_file = "C:\\Users\\Chelo\\Documents\\TestFiles\\InputsTest\\Suma.cpp"
        path_inputs_file = "C:\\Users\\Chelo\\Documents\\TestFiles\\InputsTest\\SumaInputs.txt"
        path_expected_output = "C:\\Users\\Chelo\\Documents\\TestFiles\\InputsTest\\SumaOutputs.txt"

        expected_test_output = TestStatus.TEST_PASSED

        real_test_output = nibble_evaluator.test_file(path_evaluated_file,path_inputs_file,path_expected_output)

        self.assertEqual(expected_test_output,real_test_output)



    def test_calculator(self):

        path_evaluated_file = "C:\\Users\\Chelo\\Documents\\TestFiles\\InputsTest\\Calculator.cpp"
        path_inputs_file = "C:\\Users\\Chelo\\Documents\\TestFiles\\InputsTest\\CalculatorInputs.txt"
        path_expected_output = "C:\\Users\\Chelo\\Documents\\TestFiles\\InputsTest\\CalculatorOutputs.txt"

        expected_test_output = TestStatus.TEST_PASSED

        real_test_output = nibble_evaluator.test_file(path_evaluated_file,path_inputs_file,path_expected_output)

        self.assertEqual(expected_test_output,real_test_output)

    def test_for_sum(self):

        path_evaluated_file = "C:\\Users\\Chelo\\Documents\\TestFiles\\InputsTest\\ForSum.cpp"
        path_inputs_file = "C:\\Users\\Chelo\\Documents\\TestFiles\\InputsTest\\ForSumInputs.txt"
        path_expected_output = "C:\\Users\\Chelo\\Documents\\TestFiles\\InputsTest\\ForSumOutputs.txt"

        expected_test_output = TestStatus.TEST_PASSED

        real_test_output = nibble_evaluator.test_file(path_evaluated_file,path_inputs_file,path_expected_output)

        self.assertEqual(expected_test_output,real_test_output)

    pass

unittest.main()
