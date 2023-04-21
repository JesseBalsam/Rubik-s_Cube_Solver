import unittest
import main

class testmain(unittest.TestCase):

    def testHello():
    x = main.hello()
    assertEqual(x, "Hello World!")

if __name__ == '__main__':
    unittest.main()
