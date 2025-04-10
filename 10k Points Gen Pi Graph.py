import random
import matplotlib.pyplot as plt
from math import pi
import time

start = time.time()
def point_gen(): #defining boundaries so point spawns inside the square
    return [random.uniform(-1,1),random.uniform(-1,1)]

def circle(field=2): #function to check if point generated is inside or outside circle
    return (p[0] ** 2)+(p[1]**2) <= (field/2)**2

pi_estimates = [] #list that will holds all pi esimates to plot on y-axis
pts = [] #list that holds values for x-axis

for x in range(0,10001,50): #for loop that produces pi estimates for various range of points gemerated

    total = 0
    inside = 0

    while total <= x:
        p = point_gen() #point generation

        if circle(): #returns true if point inside circle
            inside += 1
            total += 1
        else: #if point is outside circle
            total += 1

    calc_pi = 4*inside/total #calculates pi estimation
    pts.append(x) #adds to list pts
    pi_estimates.append(calc_pi) #adds to list pi_estiamtes


print("Last Value:", pi_estimates[-1])
end = time.time()
print("Script Runtime:",round(end - start, 2), "seconds") #calculate script run time

#plots the graph
plt.scatter(pts,pi_estimates,s=5)
plt.plot(pts,pi_estimates)
max_x = plt.xlim()[1]
plt.ylim(2.79,3.49)
plt.hlines(pi, 0, max_x, color='black')
plt.ylabel("$\pi$")
plt.xlabel("No. of Points")
plt.title("$\pi$ estimates $\propto$ no. of points (10000)")
plt.annotate("Last Value:" + str(round(pi_estimates[-1],2)),(pts[-1]-2000,pi_estimates[-1]+0.1))
plt.show()





