class Context:
  def __init__(self, being, world, feed):
    self.being = being
    self.world = world
    self.feed = feed

class LifeEngine:
  def __init__(self, world, events, beings, feed):
    self.__world = world
    self.__event_generators = events
    self.__beings = beings
    self.__feed = feed

  def run_cycle(self):
    for event in self.__event_generators:
      event(self.__world)
    for b in self.__beings:
      b.act(Context(world = self.__world, being = b, feed = self.__feed))
    
