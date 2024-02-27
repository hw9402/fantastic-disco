a = int(input())
b = int(input())
c = int(input())

mtp = str(a*b*c)

for i in range(10):
  print(mtp.count(str(i)))