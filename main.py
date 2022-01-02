import random
import time
from os import system
words = [
##120 nouns xD
"leader",
"agency"
,"membership"
,"singer"
,"camera"
,"preparation"
,"engineering"
,"quantity"
,"highway"
,"vehicle"
,"customer"
,"assignment"
,"worker"
,"clothes"
,"unit"
,"trainer"
,"response"
,"guitar"
,"society"
,"reality"
,"perception"
,"apartment"
,"supermarket"
,"entry"
,"salad"
,"comparison"
,"health"
,"height"
,"patience"
,"driver"
,"speech"
,"writing"
,"ability"
,"pizza"
,"situation"
,"selection"
,"assistance"
,"math"
,"computer"
,"discussion"
,"fact"
,"cheek"
,"estate"
,"sector"
,"gene"
,"chemistry"
,"language"
,"woman"
,"climate"
,"warning"##50
,"editor"
,"anxiety"
,"security"
,"reputation"
,"foundation"
,"election"
,"chest"
,"industry"
,"article"
,"skill"
,"tension"
,"stranger"
,"scene"
,"psychology"
,"soup"
,"director"
,"childhood"
,"disease"
,"police"
,"promotion"
,"measurement"
,"grocery"
,"office"
,"surgery"
,"midnight"
,"variety"
,"thanks"
,"bathroom"
,"newspaper"
,"funeral"
,"injury"
,"fact"
,"government"
,"advertising"
,"tradition"
,"quantity"
,"excitement"
,"mall"
,"temperature"
,"family"
,"profession"
,"moment"
,"climate"
,"significance"
,"coffee"
,"product"
,"grandmother"
,"president"
,"method"
,"introduction"##100
,"activity"
,"oven"
,"difficulty"
,"village"
,"property"
,"instruction"
,"nature"
,"leadership"
,"committee"
,"shopping"
,"satisfaction"
,"departure"
,"excitement"
,"speech"
,"emotion"
,"investment"
,"criticism"
,"family"
,"examination"
,"week"
]
tips = [
  "Can you beat my high score of 48.4?",
  "Accuracy is key",
  "This is not a tip",
  "Make sure to check out my other programs!",
  "This program is in under 200 lines of basic Python!",
  "The starting version of this program was created in 3 hrs lol"
]
def test():
  wordsToUse = ["", "", "", "", "", "", "", "", "", ""]
  times = ["", "", "", "", "", "", "", "", "", ""]
  characters = 0
  bigNumber = 0
  accuracy = 1
  system('clear')
  for a in range(10):
    wordsToUse[a] += str(words[random.randint(0, 119)]) 
    characters += len(wordsToUse[a])
  for b in range(10):
    print("Type: " + str(wordsToUse[b]))
    s = time.time()
    typeQuery = input(">> ")
    e = time.time()
    times[b] = float(e-s)
    if wordsToUse[b].lower() != str(typeQuery):
      accuracy -= 1/10
  for c in range(10):
    bigNumber += times[c]
  percentAccuracy = round(accuracy * 100, 1)
  grosswpm = round((characters/5)/(bigNumber/60), 2)
  wpm = round(grosswpm * (percentAccuracy/100), 2)
  system('clear')
  print("Starting WPM: "+str(grosswpm))
  print("Accuracy: "+str(percentAccuracy)+"%")
  print("Final WPM: "+str(wpm) + "\n\n")
  home()




def home():
  print("▀█▀ ▀▄▀ █▀█ ▀█▀ █▄ █ █▀▀  ▀█▀ █▀▀ █▀▀ ▀█▀ ")
  print(" █   █  █▀▀ ▄█▄ █ ▀█ █▄█   █  ██▄ ▄██  █ ")
  print("v1.0.0")
  print("----------------------------------------")
  print("Press [ENTER] to start test")
  startQuery = input(">> ")
  if str(startQuery) == "":
    test()
home()