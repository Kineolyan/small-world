import being.simple as being
from world.world import World
from world.meat import Meat
import recipes

if __name__ == "__main__":
    b = being.Being()
    b.say_hello(None)
    b.execute('say_hello')

    w = World()
    w.add_item((1, 3), Meat(3))

    b.actions['eat'] = recipes.eat.eat
    while b.bearing != being.NORTH: b.turn_left()
    for _ in range(3): b.advance(w)
    b.do(w, 'eat')
    b.turn_right()
    b.advance(w)
    b.do(w, 'eat') # Eat again this tiem
