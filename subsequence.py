# Example 1:
#
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
#
# Input: s = "axc", t = "ahbgdc"
# Output: false

s = "axc"
t = "axcw"

list1 = [i for i in s]
list2 = [i for i in t]
count = 0


for i in list1:
    for j in list2:
        if i == j:
            count +=1

if len(list1) == count:
    print(True)
else:
    print(False)
