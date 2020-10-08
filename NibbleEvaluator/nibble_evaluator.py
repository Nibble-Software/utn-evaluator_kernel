import os
import subprocess
from sys import argv
import domain.code_test_status
from domain.tester import Tester


def test_file(path_evaluated_file,path_inputs,path_expected_outputs):

    tester = Tester(path_evaluated_file,path_inputs,path_expected_outputs)
    status = tester.run_test()
    return status




if __name__ == '__main__':
    test_file("A","B","C")
