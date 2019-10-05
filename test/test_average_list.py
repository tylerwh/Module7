import unittest
from source_file import average_list


class MyTestCase(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass
  

  def test_list(self):
    test_list = [3, 4, 6, 8, 12, 19, 72]
    self.assertAlmostEqual(average_list.average(test_list), 17.7142857)

  
if __name__ == "__main__":
    unittest.main()