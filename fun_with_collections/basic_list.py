"""
Author: Tyler Hochstetler
"""


def make_list():
  """Returns a list of user input"""
  user_list = []

  try:
    for i in range(0, 3):
      num = int(get_input())
      user_list.append(num)
  except ValueError:
    print("You done messed up.. Need an int")
    
  return user_list


def get_input():
  """Asks user for 3 inputs and returns an array of those inputs"""
  pass


if __name__ == "__main__":
    print(make_list())