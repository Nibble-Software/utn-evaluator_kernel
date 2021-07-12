import sys
sys.path.append('.')
import unittest
import domain.file_reader as file_reader
from tests.file_mocker import *

class Test1(unittest.TestCase):

    def test_read_file(self):

        inputs = '''1
2'''
        outputs = '''¡HOLA MUNDO!'''

        input_path = mock_input_file(inputs)

        output_path = mock_output_file(outputs)

        expected_result = {'inputs': ["1","2"], 'outputs': ["¡HOLA MUNDO!"]}

        real_result = file_reader.FileReader.read_files(input_path,output_path)

        self.assertEqual(expected_result,real_result)



    def test_read_only_output_file(self):

        outputs = '''¡HOLA MUNDO!'''

        output_path = mock_output_file(outputs)

        expected_result = {'inputs': None , 'outputs': ["¡HOLA MUNDO!"]}

        real_result = file_reader.FileReader.read_files(None, output_path)

        self.assertEqual(expected_result,real_result)

    pass



