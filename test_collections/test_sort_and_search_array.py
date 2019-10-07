import unittest
import array as arr 
from fun_with_collections import sort_and_search_array as s_and_s 


class TestArray(unittest.TestCase):
  def test_search_array_item_found(self):
    test_array_1 = arr.array('f', [1.2, 3.2, 5.4, 6.5, 7.8, 9.5])
    self.assertEqual(s_and_s.search_array(test_array_1, 6.5), 3)


  def test_search_array_item_not_found(self):
    test_array_1 = arr.array('f', [1.2, 3.2, 5.4, 6.5, 7.8, 9.5])
    self.assertEqual(s_and_s.search_array(test_array_1, 1.3), -1)


if __name__ == "__main__":
    unittest.main()