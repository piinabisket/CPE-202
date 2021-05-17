from exp_eval import *
import unittest


class TestCases(unittest.TestCase):

    def test_postfix(self):
        self.assertEqual(postfix_eval('5 1 2 + 4 ^ + 3 -'), 83)
        self.assertEqual(postfix_eval('5 2 *'), 10)
        self.assertEqual(postfix_eval('21 3 /'), 7)
        self.assertRaises(ValueError, postfix_eval, '5 0 /')
        self.assertRaises(PostfixFormatException, postfix_eval, '0 5')
        self.assertRaises(PostfixFormatException, postfix_eval, '1 -')
        self.assertRaises(PostfixFormatException, postfix_eval, 'a')

    def test_infix(self):
        self.assertEqual(infix_to_postfix('3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3'), '3 4 2 * 1 5 - 2 3 ^ ^ / +')
        self.assertEqual(infix_to_postfix('11 + 12'), '11 12 +')

    def test_prefix(self):
        self.assertEqual(prefix_to_postfix('* - 3 / 2 1 - / 4 5 6'), '3 2 1 / - 4 5 / 6 - *')


if __name__ == '__main__':
    unittest.main()
