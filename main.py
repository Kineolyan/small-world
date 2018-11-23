import being.simple as being
from world.world import World
from world.meat import Meat
from event.food import create_meat
import recipes
from ngin.life import LifeEngine, Context
from feed.log import log

def create_being():
  b = being.Being()
  b.actions['eat'] = recipes.eat.eat
  b.actions['move'] = recipes.move.move
  
  return b

def manual():
  b = create_being()
  b.say_hello(None)
  b._do('say_hello', None)

  w = World()
  w.add_item((1, 3), Meat(3))

  while b.bearing != being.NORTH: b.turn_left()
  for _ in range(3): b.advance()
  b._do('eat', Context(b, w, log))
  b.turn_right()
  b.advance()
  b._do('eat', Context(b, w, log)) # Eat again this time
  assert w.get((1, 3)) == None

def automate():
  w = World()
  b = create_being()
  le = LifeEngine(world = w, beings = [b], events = [create_meat], feed = log)
  for _ in range(100):
    le.run_cycle()

if __name__ == "__main__":
  print "manual execution"
  print '-' * 20
  manual()
  print '=' * 20
  print "Automated mode"
  print '-' * 20
  automate()
