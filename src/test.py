import unittest
import sys

def test():
    print "++++++++++++++++++++++++++++test+++++++++++++++++++++++++++++++++++"
    tests = unittest.TestLoader().discover('./tests', pattern='*_tests.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1

if __name__ == '__main__':
    test()
