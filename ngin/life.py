class LifeEngine:
  def __init__(self, world, events, beings):
    self.__world = world
    self.__event_generators = events
    self.__beings = beings

  def run_cycle(self):
    for event in self.__event_generators:
      event(self.__world)
    for b in self.__beings:
      b.act(self.__world)
    
