# 344. Reverse String (easy)

from typing import List

class Solution:
  def reverseString(self, s: List[str]) -> None:
    s[:] = s[::-1]

# Local tests
if __name__ == "__main__":
  solution = Solution()
  
  s1 = ["h","e","l","l","o"]
  solution.reverseString(s1)
  assert s1 == ["o","l","l","e","h"]

  s2 = ["H","a","n","n","a","h"]
  solution.reverseString(s2)
  assert s2 == ["h","a","n","n","a","H"]

  print("All tests passed!")