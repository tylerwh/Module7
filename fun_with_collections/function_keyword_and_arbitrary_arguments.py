"""
Author: Tyler Hochstetler
This program is to practice using *args and **kwargs.
"""


def average_scores(*args, **kwargs):
  """Takes in any number of arguments and calculates their average, then takes any number of keyword arguments and concatenates them to a string to be returned.
  :param scores: This captures all of the arguments and processes the average calculation.
  :param str_builder: This is the string to be concatenated and returned, adding the scores parameter on the final concatenation.
  :return: Returns the str_builder to the method call.
  """
  scores = sum(args)/len(args)
  str_builder = "Result: "

  for kw in kwargs:
    # print(kw, " : ", kwargs[kw])
    str_builder = str_builder + kw + " = " + kwargs[kw] + " "
    # print(str_builder)
    
  str_builder = str_builder + " has average score of {:.2f}".format(scores)
  # print(str_builder)
  return str_builder
  

  


if __name__ == "__main__":
    test_group_1 = average_scores(4, 3, 2, 4, name='Johnny Mac', major='Exploratory Exploration')
    test_group_2 = average_scores(9, 8, 9, 7, 4, 6, Name='Philip Smith', State='Arkansas', Major='Latin Cultures')
    test_group_3 = average_scores(8, 7, 6, 8, 9, 7, 4, Name='Steven Stephenson', School='DMACC')
    print("\n\n" + test_group_1)
    print("\n\n" + test_group_2)
    print("\n\n" + test_group_3)