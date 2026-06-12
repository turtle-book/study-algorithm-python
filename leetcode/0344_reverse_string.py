# 344. Reverse String (easy)

from typing import List

class Solution:
  def reverseString(self, s: List[str]) -> None:
    return s[::-1]

# Local tests
if __name__ == "__main__":
    solution = Solution()

    assert solution.reverseString(["h","e","l","l","o"]) == ["o","l","l","e","h"]
    assert solution.reverseString(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"]

    print("All tests passed!")