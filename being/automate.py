import inspect
from random import randint

class Automate:
  def __init__(self):
    self.actions = {}
    automated_methods = inspect.getmembers(
      self,
      predicate=(lambda e: inspect.ismethod(e) and getattr(e, 'automated', False)))
    for name, method in automated_methods:
      self.actions[name] = (lambda a, world: method(world))

  def _execute(self, action):
    self.actions[action](self, None)

  def _do(self, world, action):
    self.actions[action](self, world)

  def act(self, world):
    actions = list(self.actions.keys())
    action = actions[randint(0, len(actions) - 1)]
    self._do(world, action)

def automate_method(view):
  view.automated = True
  return view
