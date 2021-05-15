from domain.file_reader import FileReader
from domain.runners.cpprunner import CppRunner
from domain.code_test_status import TestStatus
from domain import exceptions
from domain.runnercreator import RunnerCreator

class Tester():

    def __init__(self,language,path_evaluated_file,path_inputs_file,path_expected_outputs_file):

        program_data = FileReader.read_files(path_inputs_file,path_expected_outputs_file)

        self.runner = RunnerCreator.create_runner(language,path_evaluated_file,program_data['inputs'])

        self.expected_output = program_data['outputs']


    def test_code(self):
        data = {"expected": self.expected_output, "real": self.real_output}
        print(data)
        if self.expected_output == self.real_output:
            return TestStatus.TEST_PASSED

        else:
            return TestStatus.TEST_FAILED


    def run_test(self):

        try:

            self.real_output = self.runner.run_progam()

            status = self.test_code()

            return status

        except exceptions.CompilationError :

            status = TestStatus.COMPILATION_ERROR

            return status

        except exceptions.ExecutionError:

            status = TestStatus.EXECUTION_ERROR

            return status


    pass
