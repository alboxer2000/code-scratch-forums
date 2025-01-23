class BlockStack:
    def __init__(self, blocks=None, shadows=None):
        self.blocks = [] if blocks is None else blocks
        self.shadows = [] if shadows is None else shadows
    def append(self, block):
        self.blocks.append(block)
