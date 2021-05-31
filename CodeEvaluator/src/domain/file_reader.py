import os

class FileReader():    

    def read_files(path_input_file,path_output_file):

        if path_input_file is not None:

            input_file = open(path_input_file,'rb')
            inputs = FileReader.read_lines(input_file)

            output_file = open(path_output_file,'rb')
            outputs = FileReader.read_lines(output_file)

            results = {'inputs': inputs, 'outputs' : outputs}

            input_file.close()
            output_file.close()

        else:

            output_file = open(path_output_file,'rb')
            outputs = FileReader.read_lines(output_file)

            results = {'inputs': None, 'outputs' : outputs}

            output_file.close()


        return results

    def read_lines(file):

        lines = FileReader.get_file_lines(file)

        return lines

    def get_file_lines(file):

        return [item.decode('utf-8').strip() for item in file]

    pass
