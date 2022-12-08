f = open('day-7/input.txt', 'r')

class DirectoryTree:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def get_name(self):
        return self.name

    def get_all_children(self):
        children = self.get_children()
        for child in children:
            children += child.get_all_children()
        return children

    def get_all_parents(self):
        parent = self.get_parent()
        if parent is None:
            return []
        return [parent] + parent.get_all_parents()

    def __repr__(self):
        return self.name

directory = DirectoryTree('/')
current_node = directory
path = "/"

for line in f:
  if '$ cd ..' in line:
      current_node = directory.get_parent()
      path = "".join(path.split('/')[:-2]) + "/"
  elif '$ cd /' in line:
      current_node = directory
      path = "/"
  elif '$ cd' in line:
      path += line.split('$ cd ')[1].strip() + "/"
      new_directory = DirectoryTree(path)
      current_node.add_child(new_directory)
      current_node = current_node.get_children()[len(current_node.get_children()) - 1]
      

print(directory.get_all_children())