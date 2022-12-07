f = open('day-6/input.txt', 'r')

buffer = f.readline().strip()

four_letters = ""

result = 0

for letter in buffer:
  result += 1
  four_letters += letter
  if len(four_letters) > 4:
    four_letters = four_letters[1:]
  four_letters_list = list(four_letters)
  if len(set(four_letters_list)) == 4 and len(four_letters_list) == 4:
    print(four_letters)
    break

print(result)    