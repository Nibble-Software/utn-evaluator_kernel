import sys
import unittest
import nibble_evaluator
import os
from domain.code_test_status import TestStatus
from domain.runners.cpprunner import CppRunner

class Test0(unittest.TestCase):

    def test_1(self):
        path = "C:\\Users\\Chelo\\Documents\\TestFiles\\HolaMundo.cpp"
        cpp_runner = CppRunner(path,None)
        cpp_runner.compile_program(path)


    pass

unittest.main()
