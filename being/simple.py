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
    # self.actions["say-hello"] = (lambda b: b.say_hello())
    # self.actions["advance"] = (lambda b: b.advance())

  def execute(self, action):
    self.actions[action](self)

  @automate_method
  def say_hello(self):
    print "Hello world"

  def advance(self):
    move = BEARINGS[self.bearing]
    self.position = move(self.position)

  def turn_right(self):
      self.bearing = (self.bearing + 1) % len(BEARINGS)

  def turn_left(self):
      new_bearing = self.bearing - 1
      if new_bearing < 0:
          new_bearing = new_bearing + len(BEARINGS)
      self.bearing = new_bearing
