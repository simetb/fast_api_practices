from typing import List

# Function that returns the sum of all the values in a list
# Parameters: 
#   items : List[int]
#   return int 
def totalItemsSum(items: List[int]):
    sum = 0
    for item in items:
        sum+=item
    return sum

# Output
print(totalItemsSum(items=[1,2,3,4,5]))