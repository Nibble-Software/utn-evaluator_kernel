
class Tester():

    def __init__(self,expected_output,real_output):
        self.expected_output = expected_output
        self.real_output = real_output

    def test_code(self):        
        return self.expected_output == self.real_output

    pass
