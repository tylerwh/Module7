"""
Author: Tyler Hochstetler
The purpose of this program is to practice using search and sort methods on lists. 
"""


def sort_list(list_to_sort):
  """Sorts the list object that is passed as argument
  :param list_to_sort: Use sort method to sort list
  :return: Returns the sorted list back to user
  """
  list_to_sort.sort()

  return list_to_sort # return statement used in order to pass the changes back to method call


def search_list(list_to_search, element_to_search_for):
  """Returns the index of the object in the list, or -1 for item not found
  :param index_to_return: takes the list_to_search argument and uses .index() list method with the element_to_search_for argument as the argument for .index()
  :return: Returns the index location of the element_to_search_for in the list_to_search, -1 if element is not found
  """
  try:
    index_to_return = list_to_search.index(element_to_search_for)
    return index_to_return
  except (ValueError, AssertionError):
    print("Element not found in list.")
    return -1


if __name__ == "__main__":
    great_list = ['d', 'f', 'z', 'b', 'e']
    find_element_in_great_list = str(search_list(great_list, 'b'))
    print(find_element_in_great_list)
    print(sort_list(great_list))