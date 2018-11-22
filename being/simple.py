from automate import Automate, automate_method

EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2

def head_north(coords):
    x, y = coords
    return x, y + 1
def head_south(coords):
    x, y = coords
    return x, y - 1
def head_east(coords):
    x, y = coords
    return x + 1, y
def head_west(coords):
    x, y = coords
    return x - 1, y
BEARINGS = [head_north, head_east, head_south, head_west]

class Being(Automate):
  def __init__(self):
    Automate.__init__(self)
    self.position = (0, 0)
    self.bearing = NORTH
    self.strength = 10

  def gain_strength(self, count):
    self.strength += count
    print "I feel powerful!!"

  @automate_method
  def say_hello(self, world = None):
    print "Hello world"

  def next_position(self):
    move = BEARINGS[self.bearing]
    return move(self.position)

  def advance(self):
    self.position = self.next_position()

  @automate_method
  def turn_right(self, world = None):
      self.bearing = (self.bearing + 1) % len(BEARINGS)

  @automate_method
  def turn_left(self, world = None):
      new_bearing = self.bearing - 1
      if new_bearing < 0:
          new_bearing = new_bearing + len(BEARINGS)
      self.bearing = new_bearing
