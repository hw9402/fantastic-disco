n = int(input())

for i in range(1, n+1):
  sum = i
  for j in list(str(i)):
    sum += int(j)
  
  if n == sum:
    print(i)
    break
    
  if n == i:
    print(0)