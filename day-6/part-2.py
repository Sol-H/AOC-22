f = open('day-6/input.txt', 'r')

buffer = f.readline().strip()

fourteen_letters = ""

result = 0

for letter in buffer:
  result += 1
  fourteen_letters += letter
  if len(fourteen_letters) > 14:
    fourteen_letters = fourteen_letters[1:]
  fourteen_letters_list = list(fourteen_letters)
  if len(set(fourteen_letters_list)) == 14 and len(fourteen_letters_list) == 14:
    print(fourteen_letters)
    break

print(result)    