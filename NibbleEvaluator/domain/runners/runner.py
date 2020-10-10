import os
import subprocess
import sys

class Runner():

    def __init__(self,path_to_run_file,inputs):
        self.path_to_run_file = path_to_run_file
        self.inputs = inputs;


    ##Methods

    def run_progam(self):

        return 0

    ##########

    def get_file_path(self):

        return self.path_to_run_file

    ##########

    def get_inputs(self):

        return self.inputs



    ##########

    def create_process(self,executable_path):

        return subprocess.Popen(executable_path,
                stdout=subprocess.PIPE,stdin=subprocess.PIPE,
                stderr=subprocess.PIPE)


    ##########

    def create_only_output_process(self,executable_path):

        return subprocess.Popen(executable_path, stdout=subprocess.PIPE)

    ##########

    def get_process_status_code(self,process):

        return process.poll()

    ##########

    def write_inputs(self,process,input_string):

        process.stdin.write(input_string.encode('utf-8'))

        process.stdin.close()

    ##########

    def read_outputs(self,process):

        data = [item.decode("latin1").strip() for item in process.stdout]

        process.stdout.close()
        process.terminate()



        return data

    ########

    def read_outputs_after_inputs(self,process):

        data = [item.decode(sys.stdout.encoding).rstrip() for item in process.stdout]

        process.terminate()

        process.stdout.close()
        process.stderr.close()

        return data

    ########
    def format_inputs_for_stdin(self):

        return ' '.join(input for input in self.get_inputs()) + "\n"

    ########

    def execution_failed(self,process_status_code):

        return process_status_code != 0

    pass
