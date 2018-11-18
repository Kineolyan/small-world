from world.meat import Meat

def eat(being, world):
  position = being.position
  item = world.get(position)
  if item != None and isinstance(item, Meat):
    q = item.quantity
    being.gain_strength(q)
    remaining = item.consume(q)
    
    if remaining == 0: world.remove_item(position)
