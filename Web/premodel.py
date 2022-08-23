import math
import random

def splitData(k):
  a = random.randrange(1, math.floor(k/2))
  b = random.randrange(1, math.floor(k/2))
  c = k - (a + b)
  return [a, b, c]

def generatePrime(min, max):
  k = False
  while k == False:
    c = random.randrange(min, max)
    for i in range(2, math.floor(math.sqrt(c))+1):
      if c % i == 0:
        k = True
    if k == True:
      k = False
    else:
      return c

def checkPrime(j):
  k = False
  while k == False:
    for i in range(2, math.floor(math.sqrt(j))+1):
      if j % i == 0:
        k = True
    if k == True:
      return False
    else:
      return True

def factorize(k):
  lis = []
  for i in range(2, math.ceil(math.sqrt(k))+1):
    if k % i == 0 and checkPrime(i) == True:
      lis.append(i)
  return list(dict.fromkeys(lis))

def phi(n): 
  k = factorize(n)
  res = n
  for i in range(0, len(k)):
    res *= 1 - (1/k[i])
  return res

def gcd(m, n):
  ml = factorize(m)
  nl = factorize(n)
  gcd = 1
  for i in range(0, len(ml)):
    for j in range(0, len(nl)):
      if ml[i] == nl[j]:
        gcd *= nl[j]
  return gcd

