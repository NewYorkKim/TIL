import random

class RandomizedSet:

    def __init__(self):
        self.tmp = []

    def insert(self, val: int) -> bool:
        if val not in self.tmp:
            self.tmp.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.tmp:
            self.tmp.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.tmp)