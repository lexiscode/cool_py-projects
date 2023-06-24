'''
Our task is to design an optimal algorithm for checking whether a given string is palindrome or not!

"A palindrome is a string that reads the same forward and backward. For example, radar or madam.
'''

def palindrome(string):
  # the whole string is reverse (step is -1)
  # if string is palindrome, return True, else False
  if string == string[::-1]:
    return True
  else:
    return False


if __name__ == '__main__':
  print(palindrome('radar'))
  print(palindrome('madam'))
  print(palindrome('car'))

  
  ##################### Expanding what is going on under the hood, alternatively
  
  def is_palindrome(string):
  
  original_string = string
  reversed_string = reverse(string)

  if original_string == reversed_string:
    return True
  else:
    return False

#Below function is the same function as one of our previous algorithms, 
#except this time we need to convert the string data to a list format with the list() function
def reverse(data):
  # convert the palindrome data to a list format
  data = list(data)
  # index pointing to the first item
  start_index = 0
  # index pointing to the last item
  end_index = len(data) - 1

  while end_index > start_index:
    
    # keep swapping the items
    data[start_index], data[end_index] = data[end_index], data[start_index]
    # lowIndex keeps moving one step to the right
    start_index = start_index + 1
    # highIndex keeps moving one step to the left
    end_index = end_index - 1
  # transform the list of letters back into a string
  return ''.join(data)
    

if __name__ == '__main__':
  print(is_palindrome('radar'))
  print(is_palindrome('madam'))
  print(is_palindrome('car'))