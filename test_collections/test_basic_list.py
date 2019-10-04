import unittest
from unittest import mock
from unittest.mock import patch
import fun_with_collections.basic_list as topic1


class TestList(unittest.TestCase):
  @patch('topic1.get_input', return_value=5)
  def test_make_list(self, input):
    self.assertEqual(topic1.make_list(), [3, 3, 3])


if __name__ == "__main__":
    unittest.main()