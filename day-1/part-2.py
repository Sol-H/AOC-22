f = open('input.txt', 'r')

amounts = []

current_amount = 0

for line in f:
  num = line.strip('\n')
  if num != '':
    current_amount += int(num)
  else:
    amounts.append(current_amount)
    current_amount = 0

amounts.sort(reverse=True)

biggest_amount = amounts[0]
print(biggest_amount)

top_three_amount = amounts[0] + amounts[1] + amounts[2]
print(top_three_amount)

f.close()