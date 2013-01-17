from sys import exit

class Engine(object):
  def __init__(self, scene_map):
    self.scene_map = scene_map
  def play(self):
    current_scene = self.scene_map.opening_scene()

    while True:
      print "\n---------"
      next_scene_name = current_scene.enter()
      current_scene = self.scene_map.next_scene(next_scene_name)

class Scene(object):
  def enter(self):
    pass

class Death(Scene):
  def enter(self):
    print "You died."
    exit(0)

class CentralCorridor(Scene):
  def enter(self):
    print "You are in the Central Corridor. There is a Gothan in your way."
    return 'death'

class LaserWeaponArmory(Scene):
  def enter(self):
    pass

class TheBridge(Scene):
  def enter(self):
    pass

class EscapePod(Scene):
  def enter(self):
    pass

class Map(object):
  scenes = {
      'central_corridor': CentralCorridor(),
      'death': Death()
  }
  def __init__(self, start_scene):
    self.start_scene = start_scene
  def next_scene(self, scene_name):
    return Map.scenes.get(scene_name)
  def opening_scene(self):
    return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
