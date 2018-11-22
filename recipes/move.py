def move(being, world):
  x, y = being.next_position()
  if abs(x) <= 10 and abs(y) <= 10: being.advance()
