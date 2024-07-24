# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].



nums, target = [2,7,11,15], 9


def twoSum(nums, target):
    check = {}
    for i, num in enumerate(nums):
        minimum_val = target - num
        if minimum_val in check:
            return [check[minimum_val], i]
        check[num] = i

result = twoSum(nums,target)

print(result)
