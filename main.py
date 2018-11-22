import being.simple as being
from world.world import World
from world.meat import Meat
from event.food import create_meat
import recipes
from ngin.life import LifeEngine

def create_being():
  b = being.Being()
  b.actions['eat'] = recipes.eat.eat
  b.actions['move'] = recipes.move.move
  
  return b

def manual():
  b = create_being()
  b.say_hello(None)
  b._execute('say_hello')

  w = World()
  w.add_item((1, 3), Meat(3))

  while b.bearing != being.NORTH: b.turn_left()
  for _ in range(3): b.advance()
  b._do(w, 'eat')
  b.turn_right()
  b.advance()
  b._do(w, 'eat') # Eat again this time
  assert w.get((1, 3)) == None

def automate():
  w = World()
  b = create_being()
  le = LifeEngine(world = w, beings = [b], events = [create_meat])
  for _ in range(10):
    le.run_cycle()

if __name__ == "__main__":
  print "manual execution"
  print '-' * 20
  manual()
  print '=' * 20
  print "Automated mode"
  print '-' * 20
  automate()
