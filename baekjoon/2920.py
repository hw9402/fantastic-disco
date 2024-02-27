nums = list(map(int, input().split()))
temp = 0

for i in range(1, 9):
  if nums[i-1] != i:
    temp = 1

if temp == 1:
  for i in range(8, 0, -1):
    if nums[8-i] != i:
      temp = 2
      
print("ascending" if temp == 0 else ("descending" if temp == 1 else "mixed"))