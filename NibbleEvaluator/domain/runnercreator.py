import domain.runners

class RunnerCreator():

    def create_runner(language,path_evaluated_file,inputs):

        if(language == "c++"):

            return domain.runners.CppRunner(path_evaluated_file,inputs)

        elif(language == "python"):

            return domain.runners.PyRunner(path_evaluated_file,inputs)

        else:

            return None

    pass
