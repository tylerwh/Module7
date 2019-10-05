import unittest
from unittest import mock
from unittest.mock import patch
import fun_with_collections.basic_list_exception as topic2


class TestListExceptions(unittest.TestCase):
  @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab') # Testing that ValueError is raised when input is non-numeric
  def test_make_list_non_numeric(self, input):
    with self.assertRaises(ValueError):
      topic2.make_list()
  

  @patch('fun_with_collections.basic_list_exception.get_input', return_value='0') # Testing that ValueError is raised when input is less than 1
  def test_make_list_below_range(self, input):
    with self.assertRaises(ValueError):
      topic2.make_list()
  

  @patch('fun_with_collections.basic_list_exception.get_input', return_value='51') # Testing that ValueError is raised when input is more than 50
  def test_make_list_above_range(self, input):
    with self.assertRaises(ValueError):
      topic2.make_list()


if __name__ == "__main__":
    unittest.main()