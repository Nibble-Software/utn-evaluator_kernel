from domain.runners.runner import Runner
from domain import exceptions
import os
import subprocess
import sys


class CppRunner(Runner):

    def __init__(self,path_to_run_file,inputs):
        Runner.__init__(self,path_to_run_file,inputs)

        ##Change DEFAULT_EXECUTABLE_PATH according to your preffered path
        self.DEFAULT_EXECUTABLE_PATH = "C:\\Users\\Chelo\\AppData\\Local\\Temp\\cpprun.exe"

    #########
    def run_progam(self):
        execute_path = self.compile_program(self.get_file_path())

        output = self.execute_program()

        return output
    ########

    def compile_program(self,path_to_compile):

        process_status_code = subprocess.call(self.formatted_file(path_to_compile))

        if(self.execution_failed(process_status_code)):            

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

        process = subprocess.Popen(self.DEFAULT_EXECUTABLE_PATH, stdout=subprocess.PIPE)

        data = self.read_outputs(process)

        process_status_code = self.get_process_status_code(process)

        process.kill()

        if self.execution_failed(process_status_code):

            raise exceptions.ExecutionError


        return data

    ########

    def input_execution(self):

        process = subprocess.Popen(self.DEFAULT_EXECUTABLE_PATH,
                stdout=subprocess.PIPE,stdin=subprocess.PIPE,
                stderr=subprocess.PIPE)

        input_string = self.format_inputs_for_stdin()

        self.write_inputs(process,input_string)

        data = self.read_outputs_after_inputs(process)

        process_status_code = self.get_process_status_code(process)

        process.kill()

        if self.execution_failed(process_status_code):

            raise exceptions.ExecutionError



        return data

    ########

    def execution_failed(self,process_status_code):

        return process_status_code != 0

    ########

    def formatted_file(self,path_to_compile):

        return "g++ {path} -o {executable}".format(path=path_to_compile,executable =self.DEFAULT_EXECUTABLE_PATH)

    ########

    def format_inputs_for_stdin(self):

        return ' '.join(input for input in self.get_inputs()) + "\n"

    ########

    def write_inputs(self,process,input_string):

        process.stdin.write(input_string.encode('utf-8'))

        process.stdin.close()

    ########

    def read_outputs(self,process):

        data = [item.decode("latin1").strip() for item in process.stdout]

        process.terminate()

        process.stdout.close()

        return data

    ########

    def read_outputs_after_inputs(self,process):

        data = [item.decode(sys.stdout.encoding).rstrip() for item in process.stdout.readlines()]

        process.terminate()

        process.stdout.close()
        process.stderr.close()

        return data

    ########

    def get_process_status_code(self,process):
        return process.poll()

    pass
