# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

s = "A man, a plan, a canal: Panama"

ready = ""

for i in s:
    if i.isalpha() or i.isnumeric():
        ready += i.lower()

left = 0
right = len(ready) - 1

while left < right:
    if ready[left] == ready[right]:
        left += 1
        right -= 1
    else:
        print("not pol")
        break

