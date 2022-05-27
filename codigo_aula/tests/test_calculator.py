import unittest
import calculator

class Test_calculator(unittest.TestCase):
    
    def test_multiply(self):
            
        a=1
        b=2

        result=calculator.multiply(a,b)
        self.assertTrue(result==2)

    def test_divide_error(self):
            a=3
            b=0

            with self.assertRaises(ZeroDivisionError):#specific to check if the expected errors occurs
                calculator.divide(a,b)

            # self.assertRaises(ZeroDivisionError)
    def test_sum(self):
        a=2
        b=1
        result=calculator.sum(a,b)
        print(result)
        self.assertTrue(result==3)

if __name__ =='__main__':
    unittest.main()
