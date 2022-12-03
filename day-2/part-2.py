F = open('input.txt', 'r')

score = 0

for line in F:
  opponent_shape = line[0]
  outcome = line[2]

  if outcome == 'X': # loss
    if opponent_shape == 'A':
      # I go scissors
      score += 3
    elif opponent_shape == 'B':
      # I go rock
      score += 1
    elif opponent_shape == 'C':
      # I go paper
      score += 2
    else:
      print('error')

  elif outcome == 'Y': # draw
    score += 3
    if opponent_shape == 'A':
      # I go rock
      score += 1
    elif opponent_shape == 'B':
      # I go paper
      score += 2
    elif opponent_shape == 'C':
      # I go scissors
      score += 3
    else:
      print('error')
  
  elif outcome == 'Z': # win
    score += 6
    if opponent_shape == 'A':
      # I go paper
      score += 2
    elif opponent_shape == 'B':
      # I go scissors
      score += 3
    elif opponent_shape == 'C':
      # I go rock
      score += 1
    else:
      print('error')

F.close()

print(score)