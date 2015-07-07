# def count(x):
#   # returns a list from 1 to x
#   nums = [i for i in range(1, x+1)]
#   return nums
def count(x):
  # returns a list from 1 to x
  nums = [i for i in range(1, x+1)]
  return nums


def get5():
  x = 1
  def add4(x):
    return x+4
  return add4(x)

class SquareInt():
  def __init__(self, num):
    self.int = num

  def square(self):
    return self.int * self.int

  def sqsq(self):
    return self.int * self.int * self.int * self.int

class Count():
  def __init__(self, start_int):
    self.start_int = start_int
    self.current_int = start_int

  def addOne(self):
    self.current_int += 1
    return self.current_int

  def addX(self, X):
    self.current_int += X
    return self.current_int


def test():
  #student submitted hw tests here
  pass

