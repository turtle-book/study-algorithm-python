# 125. Valid Palindrome (easy)

import re

class Solution:
  def isPalindrome(self, s: str) -> bool:
    s_filtered = re.sub(r"[^A-Za-z0-9]", "", s).lower()
    s_reversed = s_filtered[::-1]
    return s_filtered == s_reversed

# Local tests
if __name__ == "__main__":
    solution = Solution()

    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True
    assert solution.isPalindrome("race a car") == False
    assert solution.isPalindrome(" ") == True

    print("All tests passed!")