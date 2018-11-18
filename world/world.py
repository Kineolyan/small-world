class World:
  def __init__(self):
    self.__items = {}

  def get(self, position):
    return self.__items.get(position, None)

  def add_item(self, position, item):
    if not position in self.__items:
      self.__items[position] = item
      return self
    else:
      raise Exception("item already defined at {}".format(position))

  def remove_item(self, position):
    del self.__items[position]
