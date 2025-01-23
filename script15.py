# script 1
list = ["Apple", "Banana", 1, 2, True, "Blue", "Scratch", 56, "Joshisaurio"]
list.append("Follow me!")
print(list)
#Output:
["Apple", "Banana", 1, 2, True, "Blue", "Scratch", 56, "Joshisaurio", "Follow me!"]

# script 2
class BlockStack:
    def __init__(self, c):
        self.blocks = []
        self.shadows = []
        self.c = c
    
    def json_constructor(self):
        return self.blocks + self.shadows
    def AddBlock(self, block):
        self.blocks.append(block)
