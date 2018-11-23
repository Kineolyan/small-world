from world.meat import Meat

def eat(context):
  being = context.being
  world = context.world

  position = being.position
  item = world.get(position)
  if item != None and isinstance(item, Meat):
    q = item.quantity
    being.gain_strength(q)
    remaining = item.consume(q)
    
    if remaining == 0: world.remove_item(position)
    context.feed(being, 'eat', 'eating all of the meat')
  else:
    context.feed(being, 'eat', 'nothing to eat here')
