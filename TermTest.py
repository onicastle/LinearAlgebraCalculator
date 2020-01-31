import unittest
import Term
import numpy as np
from Term import Term
import time

item1 = Term(0,0)
item2 = Term(4,5)
item2 =  Term()


class SomeTest(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def testOne(self):
        time.sleep(1)
        self.assertNotEqual(item2.evaluate(1), 4**5)

    def testTwo(self):
        time.sleep(2)
        self.assertEqual(item2.evaluate(), np.power(4,5))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SomeTest)
    unittest.TextTestRunner(verbosity=0).run(suite)

