f = open('day-8/input.txt', 'r')

lines = f.read().split('\n')

visible_trees = 0
scenic_scores = []

for row in lines:

  for i in range(len(row)):
    top = True
    below = True
    left = True
    right = True

    tree = int(row[i])
    scenic_score = []

    for j in range(i-1, -1, -1):
      if int(row[j]) >= tree:
        left = False
        scenic_score.append(i - j)
        break
    if left == True:
      scenic_score.append(i)
    for j in range(i+1, len(row)):
      if int(row[j]) >= tree:
        right = False
        scenic_score.append(j - i)
        break
    if right == True:
      scenic_score.append(len(row) - i - 1)
    if lines.index(row) > 0:
      for j in range(lines.index(row)-1, -1, -1):
        if int(lines[j][i]) >= tree:
          top = False
          scenic_score.append(lines.index(row) - j)
          break
    if top == True:
      scenic_score.append(lines.index(row))
    if lines.index(row) < len(lines)-1:
      for j in range(lines.index(row)+1, len(lines)):
        if int(lines[j][i]) >= tree:
          below = False
          scenic_score.append(j - lines.index(row))
          break
    if below == True:
      scenic_score.append(len(lines) - lines.index(row) - 1)
    
    score = 1
    for i in scenic_score:
      if i != 0:
        score *= i
    
    scenic_scores.append(score)

scenic_scores.sort(reverse=True)
print(scenic_scores[0])
