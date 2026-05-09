class PackingStrategy:
    @staticmethod
    def calculate_n(ct, ch, cu):
        # Porting the THU Packing Puzzle logic to the agent's brain
        return (2 * ct) + (3 * ch) + (3 * cu)
