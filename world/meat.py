class Meat:
  def __init__(self, quantity):
    self.__quantity = quantity

  @property
  def quantity(self):
    return self.__quantity

  def consume(self, quantity):
    if quantity == None: quantity = self.quantity

    if self.__quantity >= quantity:
      self.__quantity -= quantity
      return self.__quantity
    else:
      raise Exception("Cannot consume more meat than present")
  