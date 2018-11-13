class Being(object):
  def __init__(self):
    self.actions = {
      "say-hello": (lambda b: b.say_hello())
    }

  def execute(self, action):
    self.actions[action](self)

  def say_hello(self):
    print "Hello world"
