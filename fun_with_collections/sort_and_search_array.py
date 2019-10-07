"""
Author: Tyler Hochstetler
The purpose of this program is to explore arrays and their functions
"""
import array as arr


def sort_array(array_to_sort):
  """Will sort the list and return the sorted list
  :return: Returns sorted array in ascending order
  """
  # print(sorted(array_to_sort))
  return sorted(array_to_sort)


def search_array(array_to_search, element_to_search):
  """Will return the index of the object in the list or a -1 if the item is not found.
  :param index_to_return: Variable used to hold index location of the element being searched for.
  :return: Returns the index_to_return if element is found, or -1 if element is not found. 
  """
  print(type(array_to_search))
  try:
    index_to_return = array_to_search.index(element_to_search)
    return index_to_return
  except (ValueError, AssertionError):
    print("Element not found in array.")
    return -1


if __name__ == "__main__":
    pass