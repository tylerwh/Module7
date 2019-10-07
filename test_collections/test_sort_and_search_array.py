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
  

  def test_sort_array(self):
    test_array_2 = arr.array('i', [5, 6, 7, 1, 3, 9])
    self.assertEqual(s_and_s.sort_array(test_array_2), [1, 3, 5, 6, 7, 9])


if __name__ == "__main__":
    unittest.main()