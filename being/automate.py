import inspect
from random import randint
from ngin.life import Context

def name_generator():
  i = 0
  while True:
    i += 1
    yield "b-{}".format(i)

def curry_ctx(being, action, context):
  if context != None:
    assert being == context.being

    new_feed = lambda msg: context.feed(being, action, msg)
    return Context(context.being, context.world, new_feed)
  else:
    return None

class Automate:
  generator = name_generator()

  def __init__(self, name = None):
    self.name = name if name != None else next(Automate.generator)
    self.actions = {}

    automated_methods = inspect.getmembers(
      self,
      predicate=(lambda e: inspect.ismethod(e) and getattr(e, 'automated', False)))
    for name, method in automated_methods:
      self.actions[name] = (lambda context: method(curry_ctx(self, name, context)))

  def _do(self, action, context):
    self.actions[action](context)

  def act(self, context):
    actions = list(self.actions.keys())
    action = actions[randint(0, len(actions) - 1)]
    self._do(action, context)

def automate_method(view):
  view.automated = True
  return view
