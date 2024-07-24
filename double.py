# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

nums = [1,2,3,1]

x = set()

for i in nums:
    if i in x:
        print("True")
    else:
        x.add(i)




