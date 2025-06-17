import random

class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}  # Maps value to its index in list
        self.values = []        # List to store values

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        # Swap the value with the last one
        index = self.val_to_index[val]
        last_val = self.values[-1]
        self.values[index] = last_val
        self.val_to_index[last_val] = index
        # Remove the last value
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
