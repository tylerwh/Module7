"""
Author: Tyler Hochstetler
The purpose of this program is to practice using tuples and arbitrary arguments for file i/o.
"""


def write_to_file(*args):
  """Takes in an argument to write to fil student_info.txt
  :param file: Holds the file/file location of the file we are going to be appending to.
  Does not return value
  """
  print("Made it here")
  file = open('student_info.txt', 'a')
  for a in args:
    print("Made it there")
    file.write(str(a) + " ")
    # print(str(a) + " ")
  file.write("\n")
  print("Made it out")

  file.close()



def get_student_info(**kwargs):
  """Takes at least one Keyword argument then gets grade info about student, calls the write_to_file() with the info obtained.
  :param student_info: Holds the kwargs information and concatenates it as a string. It is then added at the beginning of grades param list.
  :param grades: Holds the grades in a list
  :param tuple_to_send: Holds student_info and grades as a tuple and will be passed to write_to_file()
  Does not return value.
  """
  student_info = ""
  for kw in kwargs:
    student_info = kw + ": " + kwargs[kw] + " "
  sentinel = "-1"
  print("Let's Get some grades out of you.\n Enter your grades, or -1 to stop.")
  # print(student_name)
  grades = []
  grade_input = input("Enter a grade, -1 to stop: ")
  while grade_input != sentinel:
    grades.append(grade_input)
    grade_input = input("Enter a grade, -1 to stop: ")
  
  # grades.insert(0, student_info)
  # write_to_file(grades)
  # print(type(grades))
  # print(grades)
  tuple_to_send = (student_info, grades)
  write_to_file(tuple_to_send)



def read_from_file():
  """Opens the student_info.txt file and reads each line, printing it to the console.
  :param file: Holds the file/file location of the file we are going to be appending to.
  Does not return value.
  """
  file = open('student_info.txt', 'r')
  for each in file:
    print(each)
  file.close()


if __name__ == "__main__":
  get_student_info(Name='John')
  get_student_info(Name='Timothy')
  get_student_info(Name='Thomas')
  get_student_info(Name='Sebastian')
  read_from_file()

    