#Name: Conor Smith
#Date: 5/12/21
#Description: Takes a list and reverses the order

def reverse_list(num_list):
  """A function that takes a list and reverses the order by mutating the list"""
  beginning = 0
  end = len(num_list) - 1

  while beginning < end:
      object = num_list[beginning]
      num_list[beginning] = num_list[end]
      num_list[end] = object
      beginning = beginning + 1
      end = end - 1

#vals = [7, -3, 12, 9]
#reverse_list(vals)
#print(vals)  # This should print [9, 12, -3, 7]