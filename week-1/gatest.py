# Python3 code to demonstrate 
# Grouping Anagrams 
# using defaultdict() + sorted() + values() 
from collections import defaultdict 

# initializing list 
test_list = ['lump', 'eat', 'me', 'tea', 'em', 'plum'] 

# printing original list 
print("The original list : " + str(test_list)) 

# using defaultdict() + sorted() + values() 
# Grouping Anagrams 
temp = defaultdict(list) 
print(temp)
print(str(sorted(test_list)))