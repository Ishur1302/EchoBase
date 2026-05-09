class SpatialGrid:
    def __init__(self, width=3, height=0):
        self.width = width
        self.height = height
        self.grid = []

    def add_block(self, block_type, rows):
        # Tracking the height footprint of blocks (T=2, H=3, U=3)
        self.height += rows
        self.grid.append({"type": block_type, "height_contribution": rows})
