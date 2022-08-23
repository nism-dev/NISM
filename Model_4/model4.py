# Model 4

import math
import premodel as pm
import RSA as rsa
import ast

print("######################################################")
print("######################################################")
print("##############    Model 4 Simulator    ###############")
print("##############       ver. 0.6.3        ###############")
print("######################################################")
print("######################################################\n")
def nodeFn(nodeList):
  index = len(list(nodeList))+1
  keyList = rsa.createKey()
  e = keyList[0][0]
  d = keyList[1][0]
  pq = keyList[0][1]
  newNode = [index, e, d, pq]
  nodeList.append(newNode)
  return list(nodeList)

def setNodeList(nodeList, len):
  for i in range(0, len):
    nodeList = nodeFn(nodeList)
  return list(nodeList)

def createCoord(coordList, lenC):
  indexList = []
  for i in range(1, lenC**2+1):
    indexList.append(i)
  for i in range(0, lenC):
    tempList = []
    for j in range(0, lenC):
      tempList.append(indexList[i*lenC+j])
    coordList.append(tempList)
  return coordList

def currentCoord(passedRouteList, currentPosR):
  print("Current Position:: ", currentPosR)
  passedRouteList += currentPosR
  return passedRouteList
 
resultFile = open("m4result.txt", "w")

lenC = int(input("Length of coordinate: "))
print("")
# lenIn = int(input("Number of nodes: "))
coordList = []
coordList = createCoord(coordList, lenC)
nodeList = []
nodeList = setNodeList(nodeList, lenC**2)
for i in range(0, len(coordList)):
  tempNodeList = []
  for j in range(0, lenC):
    tempNodeList.append(nodeList[i*lenC+j])
  # print(coordList[i], "  -----> ", tempNodeList)
  print(coordList[i])

print("")
senderIndex = int(input("Index of sender: "))
recieverIndex = int(input("Index of reciever: "))
for x in range(0, lenC):
  for y in range(0, lenC):
    if lenC*y + x + 1 == senderIndex:
      sCred = [x+1, y+1]
    if lenC*y + x + 1 == recieverIndex:
      rCred = [x+1, y+1]
cred = [sCred, rCred]
credR1 = cred[0]
credR12 = cred[1]
print("S, R Cred = ", cred)
# if x + y = 1 (mod 2) --> can go up
# if x + y = 0 (mod 2) --> can go dwn

nxy = abs(cred[0][0] - cred[1][0]) + abs(cred[0][1] - cred[1][1])
startCoord = cred[0]

### --> Route 2
print("\nStarting Route 2 Calculation... ")
passedRoute = []
currentPos = cred[0]

while currentPos != [cred[1][0], cred[1][1]]:

  # print("Current Position: ", currentPos)
  passedRoute = currentCoord(passedRoute, currentPos)
  nx = currentPos[0] - cred[1][0]
  ny = currentPos[1] - cred[1][1]
  if nx < 0:
    if ny < 0:
      if (currentPos[0]+currentPos[1])%2 == 0:
        currentPos[1] += 1
      elif (currentPos[0]+currentPos[1])%2 == 1:
        currentPos[0] += 1
        # print("Current Position: ", currentPos)
        passedRoute = currentCoord(passedRoute, currentPos)
        currentPos[1] += 1
    elif ny > 0:
      if (currentPos[0]+currentPos[1])%2 == 1:
        currentPos[1] -= 1
      elif (currentPos[0]+currentPos[1])%2 == 0:
        currentPos[0] += 1
        # print("Current Position: ", currentPos)
        passedRoute = currentCoord(passedRoute, currentPos)
        currentPos[1] -= 1
    else:
      currentPos[0] += 1
  elif nx > 0:
    if ny < 0:
      if (currentPos[0]+currentPos[1])%2 == 0:
        currentPos[1] += 1
      elif (currentPos[0]+currentPos[1])%2 == 1:
        currentPos[0] -= 1
        # print("Current Position: ", currentPos)
        passedRoute = currentCoord(passedRoute, currentPos)
        currentPos[1] += 1
    elif ny > 0:
      if (currentPos[0]+currentPos[1])%2 == 1:
        currentPos[1] -= 1
      elif (currentPos[0]+currentPos[1])%2 == 0:
        currentPos[0] -= 1
        # print("Current Position: ", currentPos)
        passedRoute = currentCoord(passedRoute, currentPos)
        currentPos[1] -= 1
      else:
        currentPos[0] -= 1
  else:
    if ny < 0:
      if (currentPos[0]+currentPos[1])%2 == 0:
        currentPos[1] += 1
      elif (currentPos[0]+currentPos[1])%2 == 1:
        currentPos[0] -= 1
        # print("Current Position: ", currentPos)
        passedRoute = currentCoord(passedRoute, currentPos)
        currentPos[1] += 1
    elif ny > 0:
      if (currentPos[0]+currentPos[1])%2 == 1:
        currentPos[1] -= 1
      elif (currentPos[0]+currentPos[1])%2 == 0:
        currentPos[0] -= 1
        # print("Current Position", currentPos)
        passedRoute = currentCoord(passedRoute, currentPos)
        currentPos[1] -= 1
    else:
      print("Current Position: ", currentPos)
      passedRoute = currentCoord(passedRoute, currentPos)

print("Current Position: ", currentPos)
print("\nProcess completed for :: Route 2 (SHORTEST)")
# print(passedRoute)
passedRouteList = []
for i in range(0, len(passedRoute)):
  if i % 2 == 0:
    tempList = [passedRoute[i], passedRoute[i+1]]
    passedRouteList.append(tempList)
passedRouteList.append(credR12)
print("Passed Routes: ", passedRouteList)

passedRouteList.pop(-1)
resultFile.writelines(str(passedRouteList)+"#")

def isRoutePassed(coord, passedRouteListR):
  iRPcv = False
  for i in range(0, len(passedRouteListR)):
    if coord == passedRouteListR[i]:
      iRPcv = True
  return iRPcv

def moveR1(currentPosR, xy, d,  passedRouteR):
  if xy == 'x':
    currentPosR[0] += int(d)
  elif xy == 'y':
    currentPosR[1] += int(d)
  else:
    print("ERR: Fuck you, second parameter can only be x or y.")
  passedRouteR += currentPosR
  print("Current Position:: ", currentPosR)
 
### --> Route 1
print("\nStarting Route 1 Calculation...")
currentPosR1 = passedRouteList[0]
passedRouteR1 = []
passedRouteListR1 = passedRouteList
moveR1(currentPosR1, 'x', 1, passedRouteR1)



while currentPosR1 != [cred[1][0], cred[1][1]]:
  nx = currentPosR1[0] - cred[1][0]
  ny = currentPosR1[1] - cred[1][1]
  if nx < 0:
    if ny < 0:
      if (currentPosR1[0]+currentPosR1[1])%2 == 0:
        if isRoutePassed([currentPosR1[0], currentPosR1[1]+1], passedRouteListR1) == False:
          currentPosR1[1] += 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
        else:
          if isRoutePassed([currentPosR1[0]+1, currentPosR1[1]], passedRouteListR1) == False and isRoutePassed([currentPosR1[0]-2, currentPosR1[1]], passedRouteListR1) == False:
            currentPosR1[0] += 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
            currentPosR1[0] += 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
          else:
            currentPosR1[0] -= 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
            currentPosR1[0] -= 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
      elif (currentPosR1[0]+currentPosR1[1])%2 == 1:
        if isRoutePassed([currentPosR1[0]+1, currentPosR1[1]], passedRouteListR1) == False:
          currentPosR1[0] += 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
        else:
          currentPosR1[0] -= 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
    elif ny > 0:
      if (currentPosR1[0]+currentPosR1[1])%2 == 1:
        if isRoutePassed([currentPosR1[0], currentPosR1[1]+1], passedRouteListR1) == False:
          currentPosR1[1] -= 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
        else:
          if isRoutePassed([currentPosR1[0]+1, currentPosR1[1]], passedRouteListR1) == False and isRoutePassed([currentPosR1[0]-2, currentPosR1[1]], passedRouteListR1) == False:
            currentPosR1[0] += 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
            currentPosR1[0] += 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
          else:
            currentPosR1[0] -= 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
            currentPosR1[0] -= 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
      elif (currentPosR1[0]+currentPosR1[1])%2 == 0:
        if isRoutePassed([currentPosR1[0]+1, currentPosR1[1]], passedRouteListR1) == False:
          currentPosR1[0] += 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
        else:
          currentPosR1[0] -= 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
    else:
      if isRoutePassed([currentPosR1[0]+1, currentPosR1[1]], passedRouteListR1) == False:
        currentPosR1[0] += 1
        passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
      else:
        currentPosR1[0] -= 1
        passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)  
  elif nx > 0:
    if ny < 0:
      if (currentPosR1[0]+currentPosR1[1])%2 == 0:
        if isRoutePassed([currentPosR1[0], currentPosR1[1]+1], passedRouteListR1) == False:
          currentPosR1[1] += 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
        else:
          if isRoutePassed([currentPosR1[0]-1, currentPosR1[1]], passedRouteListR1) == False and isRoutePassed([currentPosR1[0]-2, currentPosR1[1]], passedRouteListR1) == False:
            currentPosR1[0] -= 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
            currentPosR1[0] -= 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
          else:
            currentPosR1[0] += 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
            currentPosR1[0] += 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
      elif (currentPosR1[0]+currentPosR1[1])%2 == 1:
        if isRoutePassed([currentPosR1[0]-1, currentPosR1[1]], passedRouteListR1) == False:
          currentPosR1[0] -= 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
        else:
          currentPosR1[0] += 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
    elif ny > 0:
      if (currentPosR1[0]+currentPosR1[1])%2 == 0:
        if isRoutePassed([currentPosR1[0], currentPosR1[1]-1], passedRouteListR1) == False:
          currentPosR1[1] -= 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
        else:
          if isRoutePassed([currentPosR1[0]-1, currentPosR1[1]], passedRouteListR1) == False and isRoutePassed([currentPos[0]-2, currentPos[1]], passedRouteListR1) == False:
            currentPosR1[0] -= 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
            currentPosR1[0] -= 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
          else:
            currentPosR1[0] += 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
            currentPosR1[0] += 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
      elif (currentPosR1[0]+currentPosR1[1])%2 == 0:
        if isRoutePassed([currentPosR1[0]-1, currentPosR1[1]], passedRouteListR1) == False:
          currentPosR1[0] -= 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
        else:
          currentPosR1[0] += 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)  
    else:
      if isRoutePassed([currentPosR1[0]-1, currentPosR1[1]], passedRouteListR1) == False:
        currentPosR1[0] -= 1
        passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
      else:
        currentPosR1[0] += 1
        passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)  
  else:
    if ny < 0:
      if (currentPosR1[0]+currentPosR1[1])%2 == 0:
        if isRoutePassed([currentPosR1[0], currentPosR1[1]+1], passedRouteListR1) == False:
          currentPosR1[1] += 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
        else:
          if isRoutePassed([currentPosR1[0]+1, currentPosR1[1]], passedRouteListR1) == False:
            currentPosR1[0] += 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
            currentPosR1[0] += 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
          else:
            currentPosR1[0] -= 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
            currentPosR1[0] -= 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
      elif (currentPosR1[0]+currentPosR1[1])%2 == 1:
        if isRoutePassed([currentPosR1[0]+1, currentPosR1[1]], passedRouteListR1) == False:
          currentPosR1[0] += 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
        else:
          currentPosR1[0] -= 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
    elif ny > 0:
      if (currentPosR1[0]+currentPosR1[1])%2 == 1:
        if isRoutePassed([currentPosR1[0], currentPosR1[1]+1], passedRouteListR1) == False:
          currentPosR1[1] -= 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
        else:
          if isRoutePassed([currentPosR1[0]+1, currentPosR1[1]], passedRouteListR1) == False:
            currentPosR1[0] += 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
            currentPosR1[0] += 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
          else:
            currentPosR1[0] -= 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
            currentPosR1[0] -= 1
            passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
      elif (currentPosR1[0]+currentPosR1[1])%2 == 0:
        if isRoutePassed([currentPosR1[0]+1, currentPosR1[1]], passedRouteListR1) == False:
          currentPosR1[0] += 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
        else:
          currentPosR1[0] -= 1
          passedRouteR1 = currentCoord(passedRouteR1, currentPosR1)
    else:
      currentPosR1[1] += 1

print("Current Position: ", currentPosR1)
print("Process completed for :: Route 1 (RIGHT ROUTE)")
# print(passedRoute)
passedRouteListR1 = [credR1]
for i in range(0, len(passedRouteR1)):
  if i % 2 == 0:
    tempListR1 = [passedRouteR1[i], passedRouteR1[i+1]]
    passedRouteListR1.append(tempListR1)
print("Passed Routes: ", passedRouteListR1)
resultFile.writelines(str(passedRouteListR1)+"#")

### --> Route 3.. Frick

print("\nStarting Route 3 Calculation...")
currentPosR3 = [passedRoute[0], passedRoute[1]]
passedRouteR3 = []
passedRouteListR3 = []
for i in range(0, len(passedRouteListR1)):
  passedRouteList.append(passedRouteListR1[i])


moveR1(currentPosR3, 'x', -1, passedRouteListR3)
nx = currentPosR3[0] - cred[1][0]
ny = currentPosR3[1] - cred[1][1]
if (currentPosR3[0]+currentPosR3[1])%2 == 0:
  moveR1(currentPosR3, 'y', -int(ny/abs(ny)), passedRouteR3)
else:
  moveR1(currentPosR3, 'x', -1, passedRouteR3)
  moveR1(currentPosR3, 'y', -int(ny/abs(ny)), passedRouteR3)

while currentPosR3 != [cred[1][0], cred[1][1]]:
  nx = currentPosR3[0] - cred[1][0]
  ny = currentPosR3[1] - cred[1][1]
  if nx < 0:
    if ny < 0:
      if (currentPosR3[0]+currentPosR3[1])%2 == 0:
        if isRoutePassed([currentPosR3[0], currentPosR3[1]+1], passedRouteList) == False:
          currentPosR3[1] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
        else:
          if isRoutePassed([currentPosR3[0]+1, currentPosR3[1]], passedRouteList) == False and isRoutePassed([currentPosR3[0]-2, currentPosR3[1]], passedRouteList) == False:
            currentPosR3[0] += 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
            currentPosR3[0] += 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
          else:
            currentPosR3[0] -= 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
            currentPosR3[0] -= 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
      elif (currentPosR3[0]+currentPosR3[1])%2 == 1:
        if isRoutePassed([currentPosR3[0]+1, currentPosR3[1]], passedRouteList) == False:
          currentPosR3[0] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
        else:
          currentPosR3[0] -= 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
    elif ny > 0:
      if (currentPosR3[0]+currentPosR3[1])%2 == 1:
        if isRoutePassed([currentPosR3[0], currentPosR3[1]-1], passedRouteList) == False:
          currentPosR3[1] -= 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
        else:
          if isRoutePassed([currentPosR3[0]+1, currentPosR3[1]], passedRouteList) == False and isRoutePassed([currentPosR3[0]-2, currentPosR3[1]], passedRouteList) == False:
            currentPosR3[0] += 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
            currentPosR3[0] += 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
          else:
            currentPosR3[0] -= 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
            currentPosR3[0] -= 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
      elif (currentPosR3[0]+currentPosR3[1])%2 == 0:
        if isRoutePassed([currentPosR3[0]+1, currentPosR3[1]], passedRouteList) == False:
          currentPosR3[0] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
        else:
          currentPosR3[0] -= 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
    else:
      if isRoutePassed([currentPosR3[0]+1, currentPosR3[1]], passedRouteList) == False or [currentPosR3[0]+1, currentPosR3[1]] == cred[1]:
        currentPosR3[0] += 1
        passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
      else:
        if (currentPosR3[0]+currentPosR3[1])%2 == 0:
          currentPosR3[1] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
          currentPosR3[0] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
        else:
          currentPosR3[0] -= 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
          currentPosR3[1] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
          currentPosR3[0] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
  elif nx > 0:
    if ny < 0:
      if (currentPosR3[0]+currentPosR3[1])%2 == 0:
        if isRoutePassed([currentPosR3[0], currentPosR3[1]+1], passedRouteList) == False:
          currentPosR3[1] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
        else:
          if isRoutePassed([currentPosR3[0]-1, currentPosR3[1]], passedRouteList) == False and isRoutePassed([currentPosR3[0]-2, currentPosR3[1]], passedRouteList) == False:
            currentPosR3[0] -= 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
            currentPosR3[0] -= 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
          else:
            currentPosR3[0] += 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
            currentPosR3[0] += 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
      elif (currentPosR3[0]+currentPosR3[1])%2 == 1:
        if isRoutePassed([currentPosR3[0]-1, currentPosR3[1]], passedRouteList) == False:
          currentPosR3[0] -= 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
        else:
          currentPosR3[0] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
    elif ny > 0:
      if (currentPosR3[0]+currentPosR3[1])%2 == 1:
        if isRoutePassed([currentPosR3[0], currentPosR3[1]-1], passedRouteList) == False:
          currentPosR3[1] -= 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
        else:
          if isRoutePassed([currentPosR3[0]+1, currentPosR3[1]], passedRouteList) == False:
            currentPosR3[0] -= 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
          else:
            currentPosR3[0] += 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
      elif (currentPosR3[0]+currentPosR3[1])%2 == 0:
        if isRoutePassed([currentPosR3[0]-1, currentPosR3[1]], passedRouteList) == False:
          currentPosR3[0] -= 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
        else:
          currentPosR3[0] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)  
    else:
      if isRoutePassed([currentPosR3[0]-1, currentPosR3[1]], passedRouteListR3) == False:
        currentPosR3[0] -= 1
        passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
      else:
        if (currentPosR3[0]+currentPosR3[1])%2 == 0:
          currentPosR3[1] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
          currentPosR3[0] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
        else:
          currentPosR3[0] -= 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
          currentPosR3[1] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
          currentPosR3[0] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
  else:
    if ny < 0:
      if (currentPosR3[0]+currentPosR3[1])%2 == 0:
        if isRoutePassed([currentPosR3[0], currentPosR3[1]+1], passedRouteList) == False:
          currentPosR3[1] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
        else:
          if isRoutePassed([currentPosR3[0]+1, currentPosR3[1]], passedRouteList) == False:
            currentPosR3[0] += 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
            currentPosR3[0] += 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
          else:
            currentPosR3[0] -= 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
            currentPosR3[0] -= 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
      elif (currentPosR3[0]+currentPosR3[1])%2 == 1:
        if isRoutePassed([currentPosR3[0]+1, currentPosR3[1]], passedRouteList) == False:
          currentPosR3[0] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
        else:
          currentPosR3[0] -= 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
    elif ny > 0:
      if (currentPosR3[0]+currentPosR3[1])%2 == 1:
        if isRoutePassed([currentPosR3[0], currentPosR3[1]+1], passedRouteList) == False:
          currentPosR3[1] -= 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
        else:
          if isRoutePassed([currentPosR3[0]+1, currentPosR3[1]], passedRouteList) == False:
            currentPosR3[0] += 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
            currentPosR3[0] += 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
          else:
            currentPosR3[0] -= 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
            currentPosR3[0] -= 1
            passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
      elif (currentPosR3[0]+currentPosR3[1])%2 == 0:
        if isRoutePassed([currentPosR3[0]+1, currentPosR3[1]], passedRouteList) == False:
          currentPosR3[0] += 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
        else:
          currentPosR3[0] -= 1
          passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)
    else:
      passedRouteR3 = currentCoord(passedRouteR3, currentPosR3)

print("Current Position: ", currentPosR3)
print("Process completed for :: Route 3 (LEFT ROUTE)")
# print(passedRoute)
passedRouteListR3 = []
for i in range(0, len(passedRouteR3)):
  if i % 2 == 0:
    tempListR3 = [passedRouteR3[i], passedRouteR3[i+1]]
    passedRouteListR3.append(tempListR3)
print("Passed Routes: ", passedRouteListR3)
resultFile.writelines(str(passedRouteListR3))

resultFile.close()


def sendData(myCoord, data, routeList):
  print("Model4Sys:: ", myCoord, " has recieved the data.")
  if len(routeList) > 1:
    routeList.remove(routeList[0])
    data -= 1
    x = sendData(routeList[0], data, routeList)
    return x
  else:
    print("Final Data:: ", data)
    print("")
    return data


resultFilenew = open("m4result.txt")
line = resultFilenew.readline()

passedRouteL2 = ast.literal_eval(line.split('#')[0])
passedRouteL1 = ast.literal_eval(line.split('#')[1])
passedRouteL3 = ast.literal_eval(line.split('#')[2])
"""for i in range(0, len(passedRouteL2)):
  passedRouteL2[i] = ast.literal_eval(passedRouteL2[i])
for j in range(0, len(passedRouteL2)):
  passedRouteL1[j] = ast.literal_eval(passedRouteL1[j])
for k in range(0, len(passedRouteL2)):
  passedRouteL3[k] = ast.literal_eval(passedRouteL3[k])"""
resultFilenew.close()

origData = int(input("\nEnter integer data to send:: "))
dList = pm.splitData(origData)
d1 = int(dList[0])
d2 = int(dList[1])
d3 = int(dList[2])
print("")
if nxy % 2 == 1:
  a = sendData(startCoord, (nxy+1)/2 + d1, passedRouteL2)
  b = sendData(startCoord, nxy+8+d2, passedRouteL1)
  c = sendData(startCoord, (3*nxy-1)/2+d3, passedRouteL3)
  result = int(a) + int(b) + int(c)
else:
  a = sendData(startCoord, nxy/2 + d1, passedRouteL2)
  b = sendData(startCoord, nxy+8+d2, passedRouteL1)
  c = sendData(startCoord, (3*nxy)/2 + d3, passedRouteL3)
  result = int(a) + int(b) + int(c)

print("Result Possibility 1:: ", result+2)
print("Result Possibility 2:: ", result+8)
print("\n\nProcess completed for Model 4.")