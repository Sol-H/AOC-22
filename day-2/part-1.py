F = open('input.txt', 'r')

score = 0

for line in F:
  opponent_shape = line[0]
  my_shape = line[2]

  if my_shape == 'X':
    score += 1
    if opponent_shape == 'A':
      score += 3 # draw
    elif opponent_shape == 'B':
      pass # loss
    elif opponent_shape == 'C':
      score += 6 # win
    else:
      print('error')
  
  elif my_shape == 'Y':
    score += 2
    if opponent_shape == 'A':
      score += 6 # win
    elif opponent_shape == 'B':
      score += 3 # draw
    elif opponent_shape == 'C':
      pass # loss
    else:
        print('error')

  elif my_shape == 'Z':
    score += 3
    if opponent_shape == 'A':
      pass # loss
    elif opponent_shape == 'B':
      score += 6 # win
    elif opponent_shape == 'C':
      score += 3 # draw
    else:
        print('error')

  else:
    print('error')

F.close()

print(score)