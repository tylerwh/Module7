import unittest
from unittest import mock
from unittest.mock import patch
import fun_with_collections.sort_and_search_list as s_and_s 


class TestSearchAndSort(unittest.TestCase):
  #@patch('fun_with_collections.sort_and_search_list.get_input', return_value=['a', 'b', 'c'])
  def test_search_list_for_item_found(self):
    self.assertEqual(s_and_s.search_list(['a', 'b', 'c'], 'b'), 1)


  #@patch('fun_with_collections.sort_and_search_list.get_input', return_value=['a', 'b', 'c'])
  def test_search_list_for_item_not_found(self):
    self.assertEqual(s_and_s.search_list(['a', 'b', 'c'], 'd'), -1)


  def test_sort_list(self):
    list_to_sort = ['Bob', 'Cat', 'Alfred']
    self.assertEqual(s_and_s.sort_list(list_to_sort), ['Alfred', 'Bob', 'Cat'])


if __name__ == "__main__":
  unittest.main()