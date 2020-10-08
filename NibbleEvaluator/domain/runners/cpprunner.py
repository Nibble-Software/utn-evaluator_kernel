from domain.runners.runner import Runner
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

        os.system("g++ {path} -o {executable}".format(
        path=path_to_compile,
        executable =self.DEFAULT_EXECUTABLE_PATH)

        )

    ########

    def execute_program(self):

        if self.get_inputs() is None:
            data = self.no_input_execution()
        else:
            data = self.input_execution()

        return data


    def no_input_execution(self):

        process = subprocess.Popen(self.DEFAULT_EXECUTABLE_PATH, stdout=subprocess.PIPE)
        data = [item.decode("latin1").strip() for item in process.stdout]

        process.terminate()

        return data

    def input_execution(self):

        process = subprocess.Popen(self.DEFAULT_EXECUTABLE_PATH, stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)

        input_str = ' '.join(input for input in self.get_inputs()) + "\n"
        process.stdin.write(input_str.encode('utf-8'))

        process.stdin.close()

        data = [item.decode(sys.stdout.encoding).rstrip() for item in process.stdout.readlines()]

        process.terminate()

        return data


    pass
