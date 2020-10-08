import sys
sys.path.append("..")
import unittest
from app import nibble_evaluator
from domain.code_test_status import TestStatus
from domain.file_reader import FileReader

class Test1(unittest.TestCase):

    def test_read_file(self):

        test_input_path = "C:\\Users\\Chelo\\Documents\\TestFiles\\Inputs.txt"
        test_output_path = "C:\\Users\\Chelo\\Documents\\TestFiles\\Outputs.txt"

        expected_result = {'inputs': ["1","2"], 'outputs': ["¡HOLA MUNDO!"]}

        real_result = FileReader.read_files(test_input_path,test_output_path)

        self.assertEqual(expected_result,real_result)



    def test_read_only_output_file(self):

        test_output_path ="C:\\Users\\Chelo\\Documents\\TestFiles\\Outputs.txt"

        expected_result = {'inputs': None , 'outputs': ["¡HOLA MUNDO!"]}

        real_result = FileReader.read_files(None,test_output_path)

        self.assertEqual(expected_result,real_result)

    pass


unittest.main()
