
def mock_cpp_file(code):
    path = "/tmp/testfile.cpp"
    file = open(path, "w+")
    file.write(code)
    file.close()
    return path


def mock_input_file(inputs):
    path = "/tmp/input.txt"
    file = open(path, "w+")
    file.write(inputs)
    file.close()
    return path


def mock_output_file(output):
    path = "/tmp/output.txt"
    file = open(path, "w+")
    file.write(output)
    file.close()
    return path

