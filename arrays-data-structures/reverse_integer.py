'''
Our task is to design an efficient algorithm to reverse a given integer. 
For example if the input of the algorithm is 1234 then the output should be 4321
'''

user_input = int(input("Please input any number: "))

def reverse_integer(num):
  reversed_int = 0
  remainder = 0

  while(num > 0):
    # we are after the last digit in every iteration
    remainder = num % 10
    reversed_int = reversed_int * 10 + remainder
    # we remove each last digits from the original number
    # this will give us the whole number portion only
    num = num // 10  # floor div or type-casting normal div: num = int(num/10)

  return reversed_int
  
if __name__ == '__main__':
  print(reverse_integer(user_input))