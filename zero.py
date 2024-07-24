# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

numbers = [0,1,0,3,12]

def func1(nums):
    nums1 = [i for i in nums if i != 0]
    nums1.append(0)
    nums1.append(0)
    print(nums1)

func1(numbers)

# print(numbers)
