from domain.runners.runner import Runner
import os
import subprocess


class CppRunner(Runner):



    def __init__(self,path_to_run_file):
        Runner.__init__(self,path_to_run_file)

    #########
    def run_progam(self):
        execute_path = self.compile_program(self.get_file_path())

        output = self.execute_program(execute_path)

        return output
    ########

    def compile_program(self,path_to_compile):
        os.system("g++ {path} -o C:\\Users\\Chelo\\Documents\\TestFiles\\a.exe".format(path=path_to_compile) )

        return "C:\\Users\\Chelo\\Documents\\TestFiles\\a.exe"

    ########

    def execute_program(self,path_to_execute):

        data = subprocess.Popen(path_to_execute, stdout=subprocess.PIPE).communicate()[0]

        output = data.decode("latin1")

        return output


    pass
