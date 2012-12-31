import random
from sys import exit 

success = "You are now fulfilled. Nothing bothers you ever again."
distracted = "You don't have what it takes."

def random_responses(situation):
  unexpected_input = ["What does THAT MEAN?", "I doesn't thunk your riting eglish", 
                      "IMPOSSIBLE!", "Think before you type.", "Maybe you're not hungry?"]
  
  user_prompts = ["What now? -> ", "What comes next? -> "]

  responses = {'unexpected': unexpected_input, 'prompt': user_prompts}

  return random.choice(responses[situation])

def forest_start():
  print "You are on a path in the forest. You are hungry. Go forward or turn back?"
  while True:
    next = raw_input(random_responses('prompt'))
    for p in ["back", "Back"]:
      if p in next:
        field()
    for p in ["forward", "Forward"]:
      if p in next:
        clearing_1()
    print random_responses('unexpected')

def field():
  print "You emerge onto a large field. You see a house in the distance."
  while True:
    next = raw_input(random_responses('prompt'))
    for p in ["house", "House"]:
      if p in next:
        pancake_house()
    for p in ["back", "Back"]:
      if p in next:
        forest_start()
    print random_responses('unexpected')

def pancake_house():
  print "You find a house made out of pancakes. Do you live in it or eat it?"
  while True:
    next = raw_input(random_responses('prompt'))
    for p in ["eat", "Eat"]:
      if p in next:
        print "You find a bottle of pure maple syrup in the house. The debauchery that follows melts your mind, similar to the soft butter you also found.", success
        exit(0)
    for p in ["live", "Live"]:
      if p in next:
        print distracted
        exit(0)
    print random_responses('unexpected')
  
def clearing_1():
  print "You enter a small clearing in the forest. Suddenly you see a crocodile alligator is looking at you. There is a path immediately to your left that looks dark and foreboding. To your right is an ominous looking path. Beyond the crocodile alligator is a very inviting path, it looks nice."
  while True:
    next = raw_input(random_responses('prompt'))
    for p in ["interior", "drive", "chevrolet", "movie", "theatre"]:
      if p in next:
        print distracted
        exit(0)
    for p in ["back", "Back"]:
      if p in next:
        forest_start()
    for p in ["left", "Left", "dark", "Dark"]:
      if p in next:
        dark_path()
    for p in ["right", "Right", "ominous", "Ominous"]:
      if p in next:
        chili_cook_off()
    for p in ["forward", "Forward", "inviting", "Inviting", "nice", "Nice"]:
      if p in next:
        clearing_2()
    print random_responses('unexpected')

def dark_path():
  print "The path is dark and you trip. You fall into a pit of crisp, delicious bacon.", success 
  exit(0)
	
def chili_cook_off():
  print "You found a chili cook off! Wow! I like chili! You're lucky! Is it spicy?"
  next = raw_input(random_responses('prompt'))
  for p in ["Too spicy", "too spicy"]:
    if p in next: 
      print distracted
      exit(0)
  else:
    print "Yeah chili is great.", success
    exit(0)

def clearing_2():
  print "Another clearing. There's only one other path."
  while True:
    next = raw_input(random_responses('prompt'))
    for p in ["back", "Back"]:
      if p in next:
        clearing_1()
    for p in ["path", "Path", "other", "Other"]:
      if p in next:
        chili_cook_off()
    print random_responses('unexpected')

forest_start()
