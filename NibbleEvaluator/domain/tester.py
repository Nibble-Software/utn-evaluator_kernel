from domain.file_reader import FileReader
from domain.runners.cpprunner import CppRunner
from domain.code_test_status import TestStatus

class Tester():

    def __init__(self,path_evaluated_file,path_inputs_file,path_expected_outputs_file):

        program_data = FileReader.read_files(path_inputs_file,path_expected_outputs_file)

        self.runner = CppRunner(path_evaluated_file,program_data['inputs'])

        self.expected_output = program_data['outputs']


    def test_code(self):

        if self.expected_output == self.real_output:
            return TestStatus.TEST_PASSED

        else:
            return TestStatus.TEST_FAILED


    def run_test(self):

        self.real_output = self.runner.run_progam()

        status = self.test_code()

        return status



    pass
