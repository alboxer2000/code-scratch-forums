# script 1
class BlockStack:
    def __init__(self, blocks=[], shadows=[]):
        self.blocks = blocks
        self.shadows = blocks
    
    def json_constructor(self):
        return self.blocks + self.shadows
    def append(self, block):
        self.blocks.append(block)

# script 2
self.current_block_stack = BlockStack() # This code is inside a while loop

# script 3
class BlockStack:
    def __init__(self, c):
        self.blocks = []
        self.shadows = []
        self.c = c
    
    def json_constructor(self):
        return self.blocks + self.shadows
    def append(self, block):
        self.blocks.append(block)
