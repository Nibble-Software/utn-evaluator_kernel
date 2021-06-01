from .runner import Runner
import src.domain.exceptions as exceptions
import subprocess


class CppRunner(Runner):

    def __init__(self,path_to_run_file,inputs):

        Runner.__init__(self,path_to_run_file,inputs)

        ##Change DEFAULT_EXECUTABLE_PATH according to your preffered path
        self.DEFAULT_EXECUTABLE_PATH = "/tmp/cpprun.out"

    #########
    def run_progam(self):
        execute_path = self.compile_program(self.get_file_path())

        output = self.execute_program()

        return output
    ########

    def compile_program(self,path_to_compile):

        process_status_code = subprocess.call(['g++', self.get_file_path(), '-o', self.DEFAULT_EXECUTABLE_PATH])

        if self.execution_failed(process_status_code):

            raise exceptions.CompilationError


    ########

    def execute_program(self):

        if self.get_inputs() is None:
            data = self.no_input_execution()
        else:
            data = self.input_execution()

        return data

    ########

    def no_input_execution(self):

        process = self.create_only_output_process(self.DEFAULT_EXECUTABLE_PATH)

        data = self.read_outputs(process)

        process_status_code = self.get_process_status_code(process)

        process.kill()

        if self.execution_failed(process_status_code):

            raise exceptions.ExecutionError


        return data

    ########

    def input_execution(self):

        process = self.create_process(self.DEFAULT_EXECUTABLE_PATH)

        input_string = self.format_inputs_for_stdin()

        self.write_inputs(process,input_string)

        data = self.read_outputs_after_inputs(process)

        process_status_code = self.get_process_status_code(process)

        process.kill()

        if self.execution_failed(process_status_code):

            raise exceptions.ExecutionError



        return data

    ########

    def formatted_file(self,path_to_compile):

        return "g++ {path} -o {executable}".format(path=path_to_compile,executable =self.DEFAULT_EXECUTABLE_PATH)

    pass
