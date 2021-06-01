from sys import argv
from src.domain.tester import Tester


def test_file(language,path_evaluated_file,path_inputs,path_expected_outputs):

    tester = Tester(language,path_evaluated_file,path_inputs,path_expected_outputs)
    status = tester.run_test()
    return status


if __name__ == '__main__':
    output = test_file(argv[1], argv[2], argv[3])
    print(output)
