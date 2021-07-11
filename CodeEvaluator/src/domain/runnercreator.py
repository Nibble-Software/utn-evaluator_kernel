from domain.runners.cpprunner import CppRunner
from domain.runners.pyrunner import PyRunner

class RunnerCreator():

    def create_runner(language,path_evaluated_file,inputs):

        if(language == "c++"):

            return CppRunner(path_evaluated_file, inputs)

        elif(language == "python"):

            return PyRunner(path_evaluated_file, inputs)

        else:

            return None

    pass
