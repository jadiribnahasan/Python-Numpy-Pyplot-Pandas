import math
import matplotlib.pyplot as plt

attack_distance = 1000
total_time = 300
dt = 1
aca = 60
acb = 50
acc = 50
acd = 50
posA = [0, 0]
posB = [2000, 2000]
posC = [4000, 4000]
posD = [10000, 10000]


def dist(posA, posB):
    a = posB[0] - posA[0]
    b = posB[1] - posA[1]
    return math.sqrt(a**2 + b**2)


travelA = [[], []]
travelB = [[], []]
travelC = [[], []]
travelD = [[], []]
time_count = 0
flag = 0
while dist(posA, posB) > attack_distance:

    travelA[0].append(posA[0])
    travelA[1].append(posA[1])

    travelB[0].append(posB[0])
    travelB[1].append(posB[1])

    travelC[0].append(posC[0])
    travelC[1].append(posC[1])

    travelD[0].append(posD[0])
    travelD[1].append(posD[1])

    #plt.plot(posA[0], posA[1], 'go')
    #plt.plot(posB[0], posB[1], 'ro')

    if time_count > total_time:
        print('C Wins')
        flag = 1
        break

    posA[0] = posA[0] + ((aca*dt) * ((posB[0] - posA[0])/(dist(posA, posB))))
    posA[1] = posA[1] + ((aca*dt) * ((posB[1] - posA[1])/(dist(posA, posB))))

    posB[0] = posB[0] + ((acb*dt) * ((posC[0] - posB[0])/(dist(posC, posB))))
    posB[1] = posB[1] + ((acb*dt) * ((posC[1] - posB[1])/(dist(posC, posB))))

    posC[0] = posC[0] + ((acc*dt) * ((posD[0] - posC[0])/(dist(posD, posC))))
    posC[1] = posC[1] + ((acc*dt) * ((posD[1] - posC[1])/(dist(posD, posC))))

    posD[0] = posD[0] - acd * dt

    time_count += 1

if not flag:
    print('A Wins')

# plt.xkcd()
plt.style.use('fivethirtyeight')
plt.plot(travelA[0], travelA[1])
plt.plot(travelB[0], travelB[1])
plt.plot(travelC[0], travelC[1])
plt.plot(travelD[0], travelD[1])
plt.show()
