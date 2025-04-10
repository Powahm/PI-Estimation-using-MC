import random
from math import pi
import matplotlib.pyplot as plt
from matplotlib import animation

def point_gen():
    return [random.uniform(-1,1),random.uniform(-1,1)]

def circle(field=2):
    return (p[0] ** 2)+(p[1]**2) <= (field/2)**2

total = 1
inside = 0
no_of_points = 10000

def graph(i):
    global total
    global inside
    global no_of_points
    global p

    if total <= no_of_points:
        p = point_gen()
        if circle():
            inside += 1
            total += 1
            plt.scatter(p[0], p[1], c = "blue",s=25)
        else:
            total += 1
            plt.scatter(p[0], p[1], c="red",s=25)
        print(total)


anim = animation.FuncAnimation(plt.gcf(), graph)
calc_pi  = 4*inside/total
print("No. of points = ", no_of_points)
print("Estimated Value:", calc_pi)
print("Real Pi Value: ",pi)

plt.title("Monte Carlo Simulation To Calculate $\pi$")
plt.ylim(-1,1)
plt.xlim((-1,1))
plt.show()
