def bin_search(nums, target):
    left = 0;
    right = len(nums) - 1;

    while left <= right:
        mid = int((left + right)/2)
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1

        else:
            return mid

    return -1

nums = [2, 35, 234, 553, 555, 1111]
target = 35

bin_search(nums, target)

print(bin_search(nums, target))