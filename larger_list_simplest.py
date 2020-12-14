# Write a function named larger_list that has two parameters named lst1 and lst2. 
# The function should return the last element of the list that contains more elements. 
# If both lists are the same size, then return the last element of lst1.



def larger_list(lst1, lst2):
  if len(lst1)>=len(lst2):
    item = lst1[-1]
  else:
    item = lst2[-1]
  return item

# TESTS
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))  # 5  (the same)

print(larger_list([2, 4, 10, 2, 5], [-10, 2, 5, 10]))  # 5 (lst1 is larger)
