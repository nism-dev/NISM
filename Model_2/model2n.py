import math as m
import random as r

def genPrime(min, max):
    c = False
    d = False
    while c != True or d != True:
        q = r.randrange(min, max)
        c = isPrime(q)
        d = isPrime(6*q-1)
    return 6*q-1

def isPrime(p):
    c = True
    for i in range(2, p):
        if p % i == 0:
            c = False
    return c

def splitInt(n, k):
    fL = []
    for i in range(0, k-1):
        l = r.randrange(1, 2*m.floor(n/k))
        fL.append(l)
        n -= l
    fL.append(n)
    return fL

def fac(m):
    fL = []
    for i in range(1, m+1):
        if m % i == 0:
            fL.append(i)
    return fL

def sender(s, rL, mins, maxs):
    print("\nfunction_sender() starting..")
    p = genPrime(mins, maxs)
    q = p
    while q == p:
        q = genPrime(mins, maxs)
    print("variable_p => ", p)
    print("variable_q => ", q)
    aL = splitInt(p*q, 3)
    print("variable_aL => ", aL)
    dL = splitInt(s, 3)
    print("variable_dL => ", dL)
    para = reca(aL[0]+(p+q)/3, aL[1]+(p+q)/3, aL[2]+(p+q)/3)
    parb = recb((p*dL[0]+q*rL[0])*(p*rL[0]+q*dL[0]), (p*dL[1]+q*rL[1])*(p*rL[1]+q*dL[1]), (p*dL[2]+q*rL[2])*(p*rL[2]+q*dL[2]), para, rL)
    nS = 0
    for i in range(0, 3):
        nS += parb[i]
    print("\n\nFinal Result :: ", nS)
    return nS

def reca(raa, rab, rac):
    print("\nfunction_reca() starting..")
    sp = raa+rab+rac
    d = sp+1
    print("recData_sp => ", round(d))
    pL = fac(int((round(d))/36)) # --> [1, x, y, xy]
    print("variable_pL => ", pL)
    p = 6*pL[1]-1
    q = 6*pL[2]-1
    print("variable_primes => ", [p, q])
    return [p, q]

def recb(rba, rbb, rbc, pL, rL):
    print("\nfunction_recb() starting..")
    dL = []
    rbL = [rba, rbb, rbc]
    for i in range(0, 3):
        # l = (-rL[i]*(pL[0]**2+pL[1]**2)+m.sqrt((rL[i]**2)*((pL[0]**2+pL[1]**2)**2)-4*pL[0]*pL[1]*(pL[0]*pL[1]*rL[i]*rL[i]-rbL[i])))/(2*pL[0]*pL[1])
        pS = (pL[0]**2)+(pL[1]**2)
        la = pS*rL[i]
        lb = (rL[i]**2)*(pS**2)
        lc = 4*pL[0]*pL[1]*((pL[0]*pL[1]*(rL[i]**2))-rbL[i])
        ld = 2*pL[0]*pL[1]
        l = (-la+m.sqrt(lb-lc))/ld
        dL.append(l)
        print("variable_dL => ", l)
    return dL

def mF():
    print("\n------------------------------------------------------------")
    print("NISM (New Internet Security Model) Testing Model II")
    print("version 0.2.0   dev by js.tt0421_k")
    print("------------------------------------------------------------\n\n")
    iU = int(input("Enter an integer to send      :: "))
    ra = int(input("Enter the length of Route I   :: "))
    rb = int(input("Enter the length of Route II  :: "))
    rc = int(input("Enter the lenght of Route III :: "))
    minU = int(input("Enter the min value for prime :: "))
    maxU = int(input("Enter the max value for prime :: "))
    nSd = sender(iU, [ra, rb, rc], minU, maxU)
    if nSd == iU:
        print("==> Original data and Calculated data matches.")
        print("==> Success!")
    else:
        print("==> Original data and Calculated data doesn't match.")
        print("==> Test Failed!")

def tF():
    print("\n------------------------------------------------------------")
    print("NISM (New Internet Security Model) Testing Model II")
    print("> version 0.2.0   dev by js.tt0421_k")
    print("------------------------------------------------------------\n\n")
    print("> WARNING :: This is a test function. It's not a real sender.")
    u = int(input("> Number of Iterations :: "))
    j = int(input("> Dataset Minimum Value :: "))
    k = int(input("> Dataset Maximum Value :: "))
    mL = []
    for i in range(0, u):
        print("\n\n\033[46m << Test Num. ", i+1, " >>\033[0m")
        iU = r.randrange(j, k)
        ra = r.randrange(1, 100)
        rb = r.randrange(1, 100)
        rc = r.randrange(1, 100)
        print("==> S :: ", iU)
        print("==> r1 :: ", ra)
        print("==> r2 :: ", rb)
        print("==> r3 :: ", rc)
        minU = 100
        maxU = 5000
        nSd = sender(iU, [ra, rb, rc], minU, maxU)
        if round(nSd) == iU:
            print("==> Original data and Calculated data matches.")
            print("==> Success!")
            mL.append('Success')
        else:
            print("==> Original data and Calculated data doesn't match.")
            print("==> Test Failed!")
            mL.append('Failed')
    fL = []
    for l in range(0, len(mL)):
        if mL[l] != 'Success':
            fL.append(l+1)
    return [u, fL]

        
y = tF()
u = y[0]
fL = y[1]
print("\n\n> Summary\033[0m")
print("------------------------------------------------------------")
print("> Number of Iterations :: ", u)
print("> Test Run Successes :: ", u - len(fL))
print("> Test Run Fails :: ", len(fL))
print("> Failed Runs :: ", fL)
print("------------------------------------------------------------\n\n")