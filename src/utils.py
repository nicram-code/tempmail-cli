from src.imports import *

#Python Typing Text Effect - www.101computing.net/python-typing-text-effect/
def typingPrint(text):
   for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)
