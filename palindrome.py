# Check whether a string is a palindrome.
words = "madam"

if words == words[::-1]:
    print(f'"{words}" is a palindrome.')
else:
    print(f'"{words}" is not a palindrome.')


# 1. take the word
# 2. set left pointer = 0
# 3. set right pointer = length - 1
# 4. compare characters at both positions
# 5. if they are different → return False
# 6. move left forward and right backward
# 7. repeat until pointers meet
# 8. if all match → True

words = "madam"
left = 0
right = len(words) - 1
is_palindrome = True
while left < right:
    if words[left] != words[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print(f'"{words}" is a palindrome.')
else:
    print(f'"{words}" is not a palindrome.')
    