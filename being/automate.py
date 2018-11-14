import inspect

class Automate:
  def __init__(self):
    self.actions = {}
    automated_methods = inspect.getmembers(
      self,
      predicate=(lambda e: inspect.ismethod(e) and getattr(e, 'automated', False)))
    for name, method in automated_methods:
      self.actions[name] = (lambda a: method())

def automate_method(view):
  view.automated = True
  return view
