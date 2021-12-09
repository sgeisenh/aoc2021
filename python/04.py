import fileinput

lines = [line.strip() for line in fileinput.input()]

numbers = [int(num) for num in lines[0].split(',')]

boards = []
board = []
for line in lines[2:]:
  if line == '':
    boards.append(board)
    board = []
  else:
    board.append([int(num) for num in line.split()])
boards.append(board)

def checkForWin(board, numbers):
  for row in board:
    if all(col in numbers for col in row):
      return True
  for col in range(len(board[0])):
    if all(elem in numbers for elem in [row[col] for row in board]):
      return True
  if all(board[i][i] in numbers for i in range(len(board))):
    return True
  if all(board[i][len(board) - 1 - i] in numbers for i in range(len(board))):
    return True
  return False

def unmarkedSum(board, numbers):
  total = 0
  for row in board:
    for col in row:
      if col not in numbers:
        total += col
  return total

called = set()
idx = 0
lastWin = None
while idx < len(numbers):
  called.add(numbers[idx])
  idx += 1
  newBoards = []
  for board in boards:
    if checkForWin(board, called):
      if lastWin == None:
        print('Part one:', unmarkedSum(board, called) * numbers[idx - 1])
      lastWin = unmarkedSum(board, called) * numbers[idx - 1]
    else:
      newBoards.append(board)
  boards = newBoards
    
print('Part two:', lastWin)