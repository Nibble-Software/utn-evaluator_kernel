from domain.runners.runner import Runner
from domain import exceptions
import os
import subprocess
import sys

class PyRunner(Runner):

    def __init__(self,path_to_run_file,inputs):

        Runner.__init__(self,path_to_run_file,inputs)

    def run_progam(self):

        output = self.execute_program()

        return output

    def execute_program(self):

        if self.get_inputs() is None:
            data = self.no_input_execution()
        else:
            data = self.input_execution()

        return data

    def no_input_execution(self):

        process = self.create_only_output_process(self.formatted_file())

        data = self.read_outputs(process)

        process_status_code = self.get_process_status_code(process)

        process.kill()

        if self.execution_failed(process_status_code):

            raise exceptions.ExecutionError


        return data

    ########

    def input_execution(self):

        process = self.create_process(self.formatted_file())

        input_string = self.format_inputs_for_stdin()

        self.write_inputs(process,input_string)

        data = self.read_outputs_after_inputs(process)

        process_status_code = self.get_process_status_code(process)

        process.kill()

        if self.execution_failed(process_status_code):

            raise exceptions.ExecutionError



        return data

    def formatted_file(self):

        return "python {path}".format(path = self.get_file_path())

    def write_inputs(self,process,input_string):

        for item in self.get_inputs():
            string = item +"\n"
            process.stdin.write(string.encode('utf-8'))

        process.stdin.close()


    pass
