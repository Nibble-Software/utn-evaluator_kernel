import sys
sys.path.append("..")
import unittest
import main
import os
from domain.code_test_status import TestStatus


class Test0(unittest.TestCase):

    def test_failed_compilation(self):

        path_evaluated_file = "G:\\TestFiles\\SumaIndeterminadaFailedCompilation.cpp"
        path_inputs_file = "G:\\TestFiles\\Inputs.txt"
        path_expected_output = "G:\\TestFiles\\Outputs.txt"

        expected_test_output = TestStatus.COMPILATION_ERROR

        real_test_output = main.test_file(path_evaluated_file,path_inputs_file,path_expected_output)

        self.assertEqual(expected_test_output,real_test_output)

    def test_failed_execution(self):

        path_evaluated_file = "G:\\TestFiles\\SumaIndeterminadaFailedExecution.cpp"
        path_inputs_file = "G:\\TestFiles\\Inputs.txt"
        path_expected_output = "G:\\TestFiles\\Outputs.txt"

        expected_test_output = TestStatus.EXECUTION_ERROR

        real_test_output = main.test_file(path_evaluated_file,path_inputs_file,path_expected_output)

        self.assertEqual(expected_test_output,real_test_output)

    pass

unittest.main()
