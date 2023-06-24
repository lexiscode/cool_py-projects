'''
Construct an algorithm to check whether two words (or phrases) are anagrams or not!

"An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once"

For example: restful and fluster
'''

#For we to check this, we will need to sort each words in alphabetical order first, then compare the equality of the two words

#Using sorted() and then join() to convert the list to strings, without a separator 
def sortString(str):
	return ''.join(sorted(str))

#Allowing user to pick their own words/phrase
first_word = input("Type in a word or phrase: ")
second_word = input("Type in another word or phrase: ")
#Assigning and calling the user-defined function above, which arranges the words/phrase in alphabetical order
sort_first_word = sortString(first_word)
sort_second_word = sortString(second_word)
#Now lets compare their equality
if sort_first_word == sort_second_word:
  print("\nTrue")
else:
  print("\nFalse")

#######################
#ALTERNATIVELY

def is_anagram(str1,str2):
  # if the length of the strings differ - they are not anagrams
  if len(str1) != len(str2):
    return False

  # we have to sort the letters of the strings and then compare with same indexes
  # sorted() produces a sorted list by default
  #This is the bottleneck becuase it has 0(NlogN) running time
  str1 = sorted(str1)
  str2 = sorted(str2)

  # now we have to check the letters with the same indexes
  # 0(N) running time	
  for i in range(len(str1)): #or range(len(str2)) since both are of equal lengths
    if str1[i] != str2[i]:
      return False
  return True

if __name__ == '__main__':
  str1 = input("Type in a word or phrase: ")
  str2 = input("Type in another word or phrase: ")

  print(is_anagram(str1,str2))

#Overall running time is 0(NlogN) + 0(N) = 0(NlogN)