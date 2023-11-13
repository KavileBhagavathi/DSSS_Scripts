import unittest
from math_quiz import generate_random_number, generate_operation, solver


class TestMathGame(unittest.TestCase):

    def test_generate_random_number(self):
        """Test if random numbers generated are within the specified range"""
        min_val = 1
        max_val = 100
        for i in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_operation(self):
        """Test if the the function returns valid operation strings"""
        control_list = ("+","-","*")
        for i in range(1000):
            rand_operation = generate_operation()
            self.assertTrue(rand_operation in control_list)

    def test_solver(self):
        """Test if the solver function outputs correct answer for given input"""
        test_cases_list = [(1,1,"+",2),(8,9,"-",-1)]
        for test_case in test_cases_list:
            solver_output = solver(test_case[0], test_case[1], test_case[2])
            self.assertTrue(type(solver_output[0]) == str) #check for datatype
            self.assertTrue(type(solver_output[1]) == int) #check for datatype
            self.assertTrue(solver_output[1] == test_case[3]) #check output val
            self.assertTrue(solver_output[0] == str(test_case[0]) + " " + 
                                                str(test_case[2]) + " " + 
                                                str(test_case[1]))
                                                #check the output problem string

if __name__ == "__main__":
    unittest.main()
