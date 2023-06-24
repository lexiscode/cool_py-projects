'''
The problem is that we want to reverse a T[] array in O(N) linear time complexity and we want the algorithm to be in-place as well
so no additional memory can be used!
For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]
'''

#We will be increasing the lowIndex by 1 and be reducing the highIndex by 1. And when the lowIndex is equal to the highIndex
#or when the lowIndex is greater than the highIndex, then the algorithm should be terminated.


def reverse(nums):
  # index pointing to the first item
  start_index = 0
  # index pointing to the last item
  end_index = len(nums) - 1

  while end_index > start_index:
    #keep swapping the items
    nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
    # lowIndex keeps moving one step to the right
    start_index = start_index + 1
    # highIndex keeps moving one step to the left
    end_index = end_index - 1

if __name__ == '__main__':
  list = [1,2,3,4,5]
  # calling the function
  reverse(list)
  print(list)

  #Time Complexity: O(N) linear running time where N is the number of indexes in the T[] array.