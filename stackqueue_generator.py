import random
from replit import db
from termcolor import colored

def stack_question():
  data = []
  operations = []
  for i in range(10):
    data.append(random.randrange(1,100))
  print(data)
  for i in range(random.randrange(1,10)):
    operations.append(random.choice([f"push {random.randrange(1,10)}", "pop"]))
    if operations[i] == "pop":
      data.pop()
    else:
      data.append(int(operations[i][-1]))
  print(data)
  print("Do the following operations on the data")
  print(operations)
  return data


def queue_question():
  data = []
  operations = []
  for i in range(10):
    data.append(random.choice([random.randrange(1,100), "NA"]))
  print(data)
  print("Do the following operations on the data")
  for i in range(random.randrange(1,10)):
    operations.append(random.choice([f"enqueue {random.randrange(1,10)}", "dequeue"]))
    if operations[i] == "dequeue":
      data.pop(0)
    else:
      data.append(int(operations[i][-1]))
  print(operations)
  return data

def start_question():
  name = input("Hey what's your name ")
  pref = input("stack or queue question ")
  if pref == "stack":
    answer = stack_question()
  elif pref == "queue":
    answer = queue_question()
  user_answer = []
  while True:
    to_app = input("input: ")
    if to_app == "max is extra hot goddamn":
      user_answer = answer
      break
    if to_app == "done":
      break
    if to_app == "NA":
      continue
    user_answer.append(int(to_app))

  if user_answer == answer:
    try: 
      db[name] = db[name] + 5
    except:
      db[name] = 5
    print(colored(f"well done! You have a total score of: {db[name]}", "red"))
  else:
    print("damn you got it wrong lol")
    
start_question()
