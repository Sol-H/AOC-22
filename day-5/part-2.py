f = open('day-5/input.txt', 'r')

class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def push_multiple(self, items):
        for i in items:
            self.items.append(i)
    def pop(self):
        return self.items.pop()
    def pop_multiple(self, amount):
        items = []
        for i in range(amount):
            items.append(self.items.pop())
        return items
    def is_empty(self):
        return self.items == []
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
    def reverse(self):
        self.items.reverse()
    def display(self):
        print(self.items)

stacks = []

for i in range(9):
  stacks.append(stack())

for line in range(8):
  current_line = f.readline().strip()
  if current_line[1] != ' ':
    stacks[0].push(current_line[1])
  if current_line[5] != ' ':
    stacks[1].push(current_line[5])
  if current_line[9] != ' ':
    stacks[2].push(current_line[9])
  if current_line[13] != ' ':
    stacks[3].push(current_line[13])
  if current_line[17] != ' ':
    stacks[4].push(current_line[17])
  if current_line[21] != ' ':
    stacks[5].push(current_line[21])
  if current_line[25] != ' ':
    stacks[6].push(current_line[25])
  if current_line[29] != ' ':
    stacks[7].push(current_line[29])
  if current_line[33] != ' ':
    stacks[8].push(current_line[33])

for s in stacks:
  s.reverse()

f.readline()
f.readline()

for line in f:
  current_line = line.strip().split(' ')
  amount = current_line[1]
  old_stack = current_line[3]
  new_stack = current_line[5]

  items = stacks[int(old_stack) -1].pop_multiple(int(amount))
  items.reverse()
  stacks[int(new_stack) -1].push_multiple(items)
  
final = ""  
for s in stacks:
  s.display()
  final += s.peek()
print(final)  