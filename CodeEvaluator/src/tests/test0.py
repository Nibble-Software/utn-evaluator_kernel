import unittest
from domain.runners.cpprunner import CppRunner
from tests.file_mocker import mock_cpp_file


class Test0(unittest.TestCase):

    def test_1(self):
        code = '''
#include <stdio.h>

int main()
{
  printf("¡HOLA MUNDO!");
  return 0;

}
'''
        code_path = mock_cpp_file(code)

        cpp_runner = CppRunner(code_path, None)
        cpp_runner.compile_program(code_path)

    pass


