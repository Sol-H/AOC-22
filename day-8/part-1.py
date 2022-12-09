f = open('day-8/input.txt', 'r')

lines = f.read().split('\n')

visible_trees = 0

for row in lines:

  for i in range(len(row)):
    top = True
    below = True
    left = True
    right = True

    tree = int(row[i])

    for j in range(i-1, -1, -1):
      if int(row[j]) >= tree:
        left = False
        break
    for j in range(i+1, len(row)):
      if int(row[j]) >= tree:
        right = False
        break
    if lines.index(row) > 0:
      for j in range(lines.index(row)-1, -1, -1):
        if int(lines[j][i]) >= tree:
          top = False
          break
    if lines.index(row) < len(lines)-1:
      for j in range(lines.index(row)+1, len(lines)):
        if int(lines[j][i]) >= tree:
          below = False
          break
    
    if top or below or left or right:
      visible_trees += 1

print(visible_trees)
