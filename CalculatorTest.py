import unittest
import numexpr as ne

class CalculatorTest(unittest.TestCase):
    def test_sum(self):
        result = ne.evaluate("2+2")
        self.assertEqual(result, [4])


    def test_sub(self):
        result = ne.evaluate("2-2")
        self.assertEqual(result, [0])
    
    def test_div(self):
        result = ne.evaluate("2/2")
        self.assertEqual(result, [1])

    def test_multiplication(self):
        result = ne.evaluate("2*2")
        self.assertEqual(result, [4])

    def test_complex(self):
        result = ne.evaluate("2+10*3-(4/2)*2")
        self.assertEqual(result, [28])
    
    def test_square(self):
        result = ne.evaluate("sqrt(25)")
        self.assertEqual(result, [5])

    def test_pow(self):
        result = ne.evaluate("2**3")
        self.assertEqual(result, [8])

    def test_error(self):
        with self.assertRaises(Exception):
            result = ne.evaluate("2*3+x")
    
    def test_sqrt_error(self):
        with self.assertWarns(RuntimeWarning):
            result = ne.evaluate("sqrt(-1)")
        

    


if __name__ == '__main__':
    unittest.main()