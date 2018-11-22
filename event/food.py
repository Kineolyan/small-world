from random import randint

from world.meat import Meat

def create_meat(world):
  pos = (randint(-10, 10), randint(-10, 10))
  if world.get(pos) == None:
    m = Meat(randint(1, 5))
    world.add_item(pos, m)
