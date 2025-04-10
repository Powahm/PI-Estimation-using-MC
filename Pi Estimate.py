import random
import time
from math import pi
import psutil

print("Started")
start = time.time()
initial_io = psutil.disk_io_counters()

def point_gen(): #defining boundaries so point spawns inside the square
    return [random.uniform(-1,1),random.uniform(-1,1)]

def circle(field=2): #function to check if point generated is inside or outside circle
    return (p[0] ** 2)+(p[1]**2) <= (field/2)**2

total = 0
inside = 0
no_of_points = 10000000000 #no. of point to generate, 10 billion


while total <= no_of_points: #loop
    p = point_gen() #point generation

    if circle(): #returns true if point inside circle
        inside += 1
        total += 1
    else: #if point is outside circle
        total += 1

    if total == 5000000000: #halfway marker
        print("More Than Halfway")

calc_pi  = 4*inside/total #calculates pi estimation

print("No. of points = ", no_of_points)
print("Estimated Pi Value:", calc_pi)
print("Real Pi Value: ",pi)

final_io = psutil.disk_io_counters()
end = time.time()
rbytes = round((final_io.read_bytes - initial_io.read_bytes)/1000000,3) #calculating total read bytes
wbytes = round((final_io.write_bytes - initial_io.write_bytes)/1000000,3) #calculating total read bytes

print("Script Runtime:",round(end - start, 2), "seconds")
print("Read Bytes:", rbytes,"MB", "; Written Bytes:",wbytes,"MB", "; Total Bytes:", rbytes+wbytes, "MB")
