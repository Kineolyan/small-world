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
BEARING_NAMES = ['North', 'East', 'South', 'West']

class Being(Automate):
  def __init__(self, name = None):
    Automate.__init__(self, name)
    self.position = (0, 0)
    self.bearing = NORTH
    self.strength = 10

  def gain_strength(self, count):
    self.strength += count
    print "I feel powerful!!"

  @automate_method
  def say_hello(self, context = None):
    if context: 
      context.feed('hello world')
    else:
      print 'hello world'

  def next_position(self):
    move = BEARINGS[self.bearing]
    return move(self.position)

  def advance(self):
    self.position = self.next_position()

  @automate_method
  def turn_right(self, context = None):
    self.bearing = (self.bearing + 1) % len(BEARINGS)
    
    if context: context.feed("looking {}".format(BEARING_NAMES[self.bearing]))

  @automate_method
  def turn_left(self, context = None):
    new_bearing = self.bearing - 1
    if new_bearing < 0:
        new_bearing = new_bearing + len(BEARINGS)
    self.bearing = new_bearing
    
    if context: context.feed("looking {}".format(BEARING_NAMES[self.bearing]))
