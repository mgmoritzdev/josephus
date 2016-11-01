import unittest
import josephus

class SimpleJosephusTestCase(unittest.TestCase):
  def setUp(self):
    self.longMessage = True

class EvenNTestCase(SimpleJosephusTestCase):  
  def runTest(self):
    self.josephus = josephus.Josephus(10)
    self.assertEqual(self.josephus.run(), 5, 'Wrong answer')
class FortyOneTestCase(SimpleJosephusTestCase):  
  def runTest(self):
    self.josephus = josephus.Josephus(41)
    self.assertEqual(self.josephus.run(), 19, 'Wrong answer')
class PowersOfTwoTestCase(SimpleJosephusTestCase):  
  def runTest(self):
    self.josephus = josephus.Josephus(8)
    self.assertEqual(self.josephus.run(), 1, 'Wrong answer')
    self.josephus = josephus.Josephus(128)
    self.assertEqual(self.josephus.run(), 1, 'Wrong answer')
    self.josephus = josephus.Josephus(1024)
    self.assertEqual(self.josephus.run(), 1, 'Wrong answer')

if __name__ == '__main__':
  unittest.main()