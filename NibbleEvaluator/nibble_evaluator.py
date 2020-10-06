import os
import subprocess
from sys import argv
import domain.code_test_status
from domain.runners.cpprunner import CppRunner
from domain.tester import Tester
from domain.code_test_status import TestStatus

def test_file(path_evaluated_file,path_inputs,path_expected_outputs):

    cpp_runner = CppRunner(path_evaluated_file)

    resultado = cpp_runner.run_progam()

    tester = Tester(path_expected_outputs,resultado)

    test_passed = tester.test_code()

    if test_passed:
        return {'status': TestStatus.TEST_PASSED, 'percentaje' : 100.00}
    else:        
        return {'status': TestStatus.TEST_FAILED, 'percentaje' : 0.00}




if __name__ == '__main__':
    test_file("A","B","C")
