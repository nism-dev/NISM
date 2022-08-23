import premodel as pm
import math

def createKey():
  p = pm.generatePrime(10, 100)
  q = pm.generatePrime(10, 100)
  e = 0
  d = 0
  for i in range(2, math.floor(pm.phi(p*q)+1)):
    if pm.gcd(i, pm.phi(p*q)) == pm.gcd(i, p*q) and pm.gcd(i, p*q) == 1:
      e = i
  for j in range(0, math.floor(pm.phi(p*q)+1)):
    if (e*j)%pm.phi(p*q) == 1:
      d = j
  return [[e, p*q], [d, p*q]]

def encrypt(e, pq, s):
  return (s**e)%(pq)

def decrypt(d, pq, k):
  return (k**d)%(pq)