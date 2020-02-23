import math
import matplotlib.pyplot as plt

attack_distance = 1000
total_time = 300
dt = 1
aca = 60
acb = 50
posA = [0,0]
posB = [10000,10000]

def dist(posA, posB):
  a = posB[0] - posA[0]
  b = posB[1] - posA[1]
  return math.sqrt(a**2 + b**2)
  


travelA = [[],[]]
travelB = [[],[]]
time_count = 0
flag = 0
while dist(posA,posB) > attack_distance:

  travelA[0].append(posA[0])
  travelA[1].append(posA[1])

  travelB[0].append(posB[0])
  travelB[1].append(posB[1])

  #plt.plot(posA[0], posA[1], 'go')
  #plt.plot(posB[0], posB[1], 'ro')

  if time_count > total_time:
    print('B Wins')
    flag = 1
    break
  
  posA[0] = posA[0] + ((aca*dt) * ((posB[0] - posA[0])/(dist(posA,posB))))
  posA[1] = posA[1] + ((aca*dt) * ((posB[1] - posA[1])/(dist(posA,posB))))
  posB[0] = posB[0] - acb * dt

  time_count += 1

if not flag:
    print('A Wins')

#plt.xkcd()
plt.style.use('fivethirtyeight')
plt.plot(travelA[0], travelA[1])
plt.plot(travelB[0], travelB[1])
plt.show()
