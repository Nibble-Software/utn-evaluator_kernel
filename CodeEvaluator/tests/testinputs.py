import unittest
from src import codeevaluator
from src.domain.code_test_status import TestStatus
from tests.file_mocker import *


class Test0(unittest.TestCase):

    def test_with_two_inputs(self):

        code = '''
#include <stdio.h>

int main()
{
int a,b;

scanf("%d",&a);
scanf("%d",&b);

printf("%d",a+b);
return 0;
}

'''
        inputs = "2\n3"

        outputs = "5"

        code_path = mock_cpp_file(code)

        input_path = mock_input_file(inputs)

        output_path = mock_output_file(outputs)

        expected_test_output = TestStatus.TEST_PASSED

        real_test_output = codeevaluator.test_file("c++", code_path, input_path, output_path)

        self.assertEqual(str(expected_test_output),str(real_test_output))

    def test_calculator(self):

        code = '''
#include <stdio.h>
int main()
{
int a,b;

scanf("%d",&a);
scanf("%d",&b);

printf("%d\\n",a+b);
printf("%d\\n",a-b);
printf("%d\\n",a*b);
printf("%.2f\\n",(float)a/b);	

return 0;

}
'''
        inputs = "4\n4"

        outputs = "8\n0\n16\n1.00"

        code_path = mock_cpp_file(code)

        input_path = mock_input_file(inputs)

        output_path = mock_output_file(outputs)

        expected_test_output = TestStatus.TEST_PASSED

        real_test_output = codeevaluator.test_file("c++", code_path, input_path, output_path)

        self.assertEqual(str(expected_test_output),str(real_test_output))

    def test_for_sum(self):

        code = '''
#include <stdio.h>

int main()
{
int a,b,cantidad;

scanf("%d",&cantidad);

for(int i = 0; i< cantidad; i++)
{
scanf("%d %d",&a,&b);
printf("%d\\n",a+b);
}

return 0;
}

'''
        inputs = '''3
2 2
3 3
4 4 
'''
        outputs = '''4
6
8
'''
        code_path = mock_cpp_file(code)

        input_path = mock_input_file(inputs)

        output_path = mock_output_file(outputs)

        expected_test_output = TestStatus.TEST_PASSED

        real_test_output = codeevaluator.test_file("c++", code_path, input_path, output_path)

        self.assertEqual(str(expected_test_output), str(real_test_output))

    pass

