"""docstring"""


def average(a_list):
  sum = 0
  count = 0
  for num in a_list:
    sum += num
    count += 1
  
  return sum / count


def other_average(*args, **kwargs):
  for a in args:
    print(a)
  for key, value in kwargs.items():
    print("Key is " + key + " Value is " + value)


if __name__ == "__main__":
    test_list = [3, 4, 6, first_name='Tyler', last_name='Hochstetler', major="BIS"]
    print(other_average(3, 4, 6, first_name='Tyler', last_name='Hochstetler', major="BIS"))