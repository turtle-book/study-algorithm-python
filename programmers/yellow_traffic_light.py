# Lv.1 노란 신호등
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/468371?language=python3

import math

def solution(signals):
  quotient = list(map(sum, signals))
  remainder_max = list(map(lambda x: sum(x[:2]), signals))
  remainder_min = list(map(lambda x: x[0] + 1, signals))

  for n in range(remainder_min[0], math.lcm(*quotient)):
    if all(rmn <= n % q <= rmx for q, rmn, rmx in zip(quotient, remainder_min, remainder_max)):
      return n
    
  return -1

# 테스트
print(solution([[2, 1, 2], [5, 1, 1]]) == 13)
print(solution([[2, 3, 2], [3, 1, 3], [2, 1, 1]]) == 11)
print(solution([[3, 3, 3], [5, 4, 2], [2, 1, 2]]) == 193)
print(solution([[1, 1, 4], [2, 1, 3], [3, 1, 2], [4, 1, 1]]) == -1)
