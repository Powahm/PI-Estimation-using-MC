import random
from math import pi
import matplotlib.pyplot as plt


def point_gen(): #defining boundaries so point spawns inside the square
    return [random.uniform(-1,1),random.uniform(-1,1)]

def circle(field=2): #function to check if point generated is inside or outside circle
    return (p[0] ** 2)+(p[1]**2) <= (field/2)**2

total = 0
inside = 0
no_of_points = 10000 #no. of point to generate


while total <= no_of_points:
    p = point_gen() #generate point
    if circle(): #returns true if inside circle
        inside += 1
        total += 1
        plt.scatter(p[0], p[1], c = "blue",s=2)
    else: #if point outside circle
        total += 1
        plt.scatter(p[0], p[1], c="red",s=2)


calc_pi  = 4*inside/total #calculation for Pi

print("No. of points = ", no_of_points)
print("Estimated Value:", calc_pi)
print("Real Pi Value: ",pi)

#lines of code for plot
axs = plt.subplot()
circle1 = plt.Circle((0, 0), 1, color='black', fill=False)
axs.add_artist(circle1)
plt.title("Monte Carlo Simulation To Calculate PI")
plt.ylim(-1,1)
plt.xlim(-1,1)
plt.show()

