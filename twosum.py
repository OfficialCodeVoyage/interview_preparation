def twoSum(nums, int):
    ddd = {}
    count = 0
    for i in nums:
        ddd[i] = count
        count += 1



    print(ddd)


def twoSum(nums, result):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == result:
                # print(f"{nums[i]}, {nums[j]}")
                return i, j

# Example usage
nums = [2, 7, 11, 15]
target = 9
twoSum(nums, target)
print(twoSum(nums, target))

#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].