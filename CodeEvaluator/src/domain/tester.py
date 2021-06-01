import src.domain.file_reader as file_reader
import src.domain.code_test_status as test_status
import src.domain.exceptions as exceptions
import src.domain.runnercreator as runner_creator


class Tester:

    def __init__(self, language, path_evaluated_file, path_inputs_file, path_expected_outputs_file):

        program_data = file_reader.FileReader.read_files(path_inputs_file, path_expected_outputs_file)

        self.runner = runner_creator.RunnerCreator.create_runner(language, path_evaluated_file, program_data['inputs'])

        self.expected_output = program_data['outputs']

    def test_code(self):
        data = {"expected": self.expected_output, "real": self.real_output}
        print(data)
        if self.expected_output == self.real_output:
            return test_status.TestStatus.TEST_PASSED

        else:
            return test_status.TestStatus.TEST_FAILED

    def run_test(self):

        try:

            self.real_output = self.runner.run_progam()

            status = self.test_code()

            return status

        except exceptions.CompilationError :

            status = test_status.TestStatus.COMPILATION_ERROR

            return status

        except exceptions.ExecutionError:

            status = test_status.TestStatus.EXECUTION_ERROR

            return status

    pass

