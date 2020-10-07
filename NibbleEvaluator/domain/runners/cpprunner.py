from domain.runners.runner import Runner
import os
import subprocess


class CppRunner(Runner):



    def __init__(self,path_to_run_file):
        Runner.__init__(self,path_to_run_file)

        ##Change DEFAULT_EXECUTABLE_PATH according to your preffered path
        self.DEFAULT_EXECUTABLE_PATH = "C:\\Users\\Chelo\\AppData\\Local\\Temp\\cpprun.exe"

    #########
    def run_progam(self):
        execute_path = self.compile_program(self.get_file_path())

        output = self.execute_program(self.DEFAULT_EXECUTABLE_PATH)

        return output
    ########

    def compile_program(self,path_to_compile):

        os.system("g++ {path} -o {executable}".format(
        path=path_to_compile,
        executable =self.DEFAULT_EXECUTABLE_PATH)

        )

    ########

    def execute_program(self,path_to_execute):

        output = []
        process = subprocess.Popen(path_to_execute, stdout=subprocess.PIPE)
        data = [item.decode("latin1").strip() for item in process.stdout]




        return data


    pass
