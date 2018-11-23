def move(context):
  being = context.being

  x, y = being.next_position()
  if abs(x) <= 10 and abs(y) <= 10: 
    being.advance()
    context.feed(being, 'move', "moving to {}".format(being.position))
  else:
    context.feed(being, 'move', 'staying in place')
