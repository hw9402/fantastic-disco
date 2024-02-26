x, y = map(int, input().split())
board = []

for _ in range(x):
  board.append(list(input()))
  
result = []

for i in range(x-7):
  for j in range(y-7):
    b_count = 0
    w_count = 0
    
    for a in range(i, i+8):
      for b in range(j, j+8):
        if (a + b) % 2 == 0: 
          if board[a][b] == 'W':
            w_count += 1
          if board[a][b] == 'B':
            b_count += 1
        else: 
          if board[a][b] == 'W':
            b_count += 1
          if board[a][b] == 'B':
            w_count += 1
      
    result.append(min(b_count, w_count))
        
print(min(result))