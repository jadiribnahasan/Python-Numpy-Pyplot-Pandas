import matplotlib.pyplot as plt
import numpy as np
import random as rand

plt.style.use('fivethirtyeight')

def f1(x):
  return -x+5

def f2(x):
  return x+5

def f3(x):
  return -x-5

def f4(x):
  return x-5

def findArea1(trials , a , b):
  hits = 0
  for i in range(trials):
    xr = rand.uniform(a , b)
    yr = rand.uniform(0 , max(f1(a) , f1(b)))
    if(yr <= f1(xr)):
        hits += 1
        plt.plot(xr , yr , 'ro')
    else:
        plt.plot(xr , yr , 'ko')

  I = (hits/trials) * (b-a) * max(f1(a) , f1(b))
  return I

def findArea2(trials , a , b):
  hits = 0
  for i in range(trials):
    xr = rand.uniform(a , b)
    yr = rand.uniform(0 , max(f2(a) , f2(b)))
    if(yr <= f2(xr)):
        hits += 1
        plt.plot(xr , yr , 'go')
    else:
        plt.plot(xr , yr , 'ko')

  I = (hits/trials) * (b-a) * max(f2(a) , f2(b))
  return I


def findArea3(trials , a , b):
  hits = 0
  for i in range(trials):
    xr = rand.uniform(a , b)
    yl = max(abs(f3(a)) , abs(f3(b)))
    yr = rand.uniform(0 , min(f3(a) , f3(b)))
    if(yr >= f3(xr)):
        hits += 1
        plt.plot(xr , yr , 'bo')
    else:
        plt.plot(xr , yr , 'ko')

  I = (hits/trials) * (b-a) * abs(min(f3(a) , f3(b)))
  return I



def findArea4(trials , a , b):
  hits = 0
  for i in range(trials):
    xr = rand.uniform(a , b)
    yr = rand.uniform(0 , min(f4(a) , f4(b)))
    if(yr >= f4(xr)):
        hits += 1
        plt.plot(xr , yr , 'yo')
    else:
        plt.plot(xr , yr , 'ko')

  I = (hits/trials) * (b-a) * abs(min(f4(a) , f4(b)))
  return I




A1 = findArea1(1000 , 0 , 5)
A2 = findArea2(1000 , -5 , 0)
A3 = findArea3(1000 , -5 , 0)
A4 = findArea4(1000 , 0 , 5)

print(A1 + A2 + A3 + A4)

plt.show()
