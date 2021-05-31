import sys
sys.path.append("..")
import unittest
from src import codeevaluator
from src.domain.code_test_status import TestStatus


class Test0(unittest.TestCase):

    @unittest.skip("needs redesign")
    def test_failed_compilation(self):

        code = '''

'''

        path_evaluated_file = "G:\\TestFiles\\SumaIndeterminadaFailedCompilation.cpp"
        path_inputs_file = "G:\\TestFiles\\Inputs.txt"
        path_expected_output = "G:\\TestFiles\\Outputs.txt"

        expected_test_output = TestStatus.COMPILATION_ERROR

        real_test_output = codeevaluator.test_file("c++", path_evaluated_file, path_inputs_file, path_expected_output)

        self.assertEqual(expected_test_output,real_test_output)

    @unittest.skip("needs redesign")
    def test_failed_execution(self):

        path_evaluated_file = "G:\\TestFiles\\SumaIndeterminadaFailedExecution.cpp"
        path_inputs_file = "G:\\TestFiles\\Inputs.txt"
        path_expected_output = "G:\\TestFiles\\Outputs.txt"

        expected_test_output = TestStatus.EXECUTION_ERROR

        real_test_output = codeevaluator.test_file("c++", path_evaluated_file, path_inputs_file, path_expected_output)

        self.assertEqual(expected_test_output,real_test_output)

    pass

