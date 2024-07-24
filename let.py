# Example 1:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].


numbers = [2,7,11,15]
target = 9
left = 0
right = len(numbers) - 1

while left < right:
    sum = numbers[left] + numbers[right]
    if sum == target:
        print(f"{numbers[left], numbers[right]}")
        break
    elif sum > target:
        right -= 1
    else:
        left +=1
