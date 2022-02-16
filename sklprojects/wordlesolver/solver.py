import random, timeit

suitable = []
guess = ""
colours = ""
green = ["", "", "", "", ""] ## (letter, pos)
yellow = ["", "", "", "", ""]
reds = ["", "", "", "", ""]

  
with open("WordleList.txt", "r") as f:
    for lines in f:
      suitable.append(lines.strip("\n"))

##input
def TakeInput(g, c):
  global guess
  global colours

  guess = g
  colours = c
  return g, c

##process input
def ProcessInput(g, c):
  for i in range(len(c)):
    if c[i] == "🟩":
      green[i] = g[i]
    elif c[i] == "🟨":
      yellow[i] = g[i]
    else:
      reds[i] = g[i]

def Guess():
  global suitable
  newlist = []

  ##check green check red check yellow or wtv
  
  suitable = CheckRedAndYellow(suitable)
  newlist = CheckGreen(suitable)

  
  if newlist:
    suitable = newlist
  guess = random.choice(suitable)
  suitable.remove(guess)
  return guess

def CheckGreen(arr):
  if green == ["", "", "", "", ""]:
      return arr
  newlist = []
  for i in range(len(arr)):
    ##print(i, len(suitable))
    can = True
    for x in range(len(green)):
      if green[x] == '':
        continue
      if green[x] != arr[i][x]:
        can = False
    if can:
        ##print(suitable[i], green)
        newlist.append(arr[i])

  return newlist
  

def CheckRedAndYellow(arr):
  temp = arr[:]
  for i in range(len(arr)):
    ##print(len(arr), i)
    for x in range(len(yellow)):

      if reds[x] == '':
        pass
      elif reds[x] in arr[i]:
        temp.remove(arr[i])
        break
      
      ## ^[arn] returns x with no a r n
      if yellow[x] == '':
        continue
      elif yellow[x] not in arr[i]:
        
        temp.remove(arr[i])
        break
      elif yellow[x] == arr[i][x]:
        temp.remove(arr[i])
        break
  return temp

  
##main
def Solve():
  
  start = timeit.default_timer()
  ProcessInput(guess, colours)
  x = Guess()
  print(timeit.default_timer() - start)


  return x

