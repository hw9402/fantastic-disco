change = int(input())
coin_type = [500, 100, 50, 10]
result = 0

for coin in coin_type:
  result += change // coin
  change %= coin
  
print(result)