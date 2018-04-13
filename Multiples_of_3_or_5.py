def solution(number):
  res = 0
  for x in range(number):
      if x % 3 == 0:
          res += x
      elif x % 5 == 0:
          res += x
  return res

print solution(20) # 78
print solution(10) # 23 
