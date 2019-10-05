"""
Author: Tyler Hochstetler
"""


def make_list():
  """Returns a list of user input
  :param user_list: List variable to hold list of user input
  :param num: temporary variable used to hold the return from get_input(), which is stored as an integer and appended to user_list
  :return: Returns user_list 
  """
  user_list = []

  try:
    for i in range(0, 3):
      num = int(get_input())
      user_list.append(num)
    return user_list
  except ValueError:
    print("You done messed up.. Need an int")
    raise ValueError
    
  # return user_list


def get_input():
  """Asks user for input and return as string.
  :param user_input: Capture integer from user input
  :return: user_input as string
  """
  user_input = input("Please input a number: ")

  return user_input


if __name__ == "__main__":
    make_a_list = make_list()
    print(make_a_list)