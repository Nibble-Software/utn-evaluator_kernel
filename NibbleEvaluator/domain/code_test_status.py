from enum import Enum

class TestStatus(Enum):

    TEST_PASSED = 0
    TEST_FAILED = 1
    COMPILATION_ERROR = 2
    EXECUTION_ERROR = 3

    pass
