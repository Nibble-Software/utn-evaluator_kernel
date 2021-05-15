import unittest
from domain.code_test_status import TestStatus
import main
from tests.file_mocker import *


class Test1(unittest.TestCase):

    def test_1(self):
        code = '''
#include <stdio.h>

int main()
{
  printf("HOLA MUNDO");
  return 0;

}
'''
        output = "HOLA MUNDO"

        code_path = mock_cpp_file(code)

        output_path = mock_output_file(output)

        expected_test_output = TestStatus.TEST_PASSED

        real_test_output = main.test_file("c++", code_path, None, output_path)

        self.assertEqual(expected_test_output, real_test_output)

    def test_multiple_outputs(self):
        code = '''
#include <stdio.h>

int main()
{
  printf("HOLA MUNDO\\n");
  printf("CHAU MUNDO");
  return 0;

}
'''
        output = "HOLA MUNDO\nCHAU MUNDO"

        code_path = mock_cpp_file(code)

        output_path = mock_output_file(output)

        expected_test_output = TestStatus.TEST_PASSED

        real_test_output = main.test_file("c++", code_path, None, output_path)

        self.assertEqual(expected_test_output, real_test_output)

    def test_one_to_five(self):
        code = '''
#include <stdio.h>

int main()
{
for(int i = 0 ; i<5 ; i++)
{
printf("%d\\n",i+1);
}
return 0;
}
'''
        output = "1\n2\n3\n4\n5"

        code_path = mock_cpp_file(code)

        output_path = mock_output_file(output)

        expected_test_output = TestStatus.TEST_PASSED

        real_test_output = main.test_file("c++",code_path, None, output_path)

        self.assertEqual(expected_test_output, real_test_output)

    pass


unittest.main()
