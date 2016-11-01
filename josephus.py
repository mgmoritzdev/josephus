import sys

class Josephus:
  def __init__(self, n):
    self.n = n
    self.soldierStatusArray = [True] * n
    self.killNext = True

  def numberOfLivingSoldiers(self, arr):
    return len(filter(self.isTrue, self.soldierStatusArray))

  def isTrue(self, x):
    return x

  def isCurrentSoldierAlive(self, index):
    return self.soldierStatusArray[index]

  def run(self):
    while self.numberOfLivingSoldiers(self.soldierStatusArray) > 1:
      for i in range(len(self.soldierStatusArray)):
        if self.isCurrentSoldierAlive(i):
          if self.killNext:
            self.killNext = False
            continue
          else:
            self.soldierStatusArray[i] = False
            self.killNext = True
    return self.soldierStatusArray.index(True) + 1