import numpy as np
# growth.py - simulation of unconstrained growth
import matplotlib.pyplot as plt
print("\nSIMULATION - Unconstrained Growth\n")
length = 100
population = 100
growth_rate = 0.1
time_step = 0.5
num_iter = length / time_step
growth_step = growth_rate * time_step

print("INITIAL VALUES:\n")
print("Simulation Length (hours): ", length)
print("Initial Population: ", population)
print("Growth Rate (per hour): ", growth_rate)
print("Time Step (part hour per step): ", time_step)
print("Num iterations (length * timestep / hour):", num_iter)
print("Growth step (growthrate per timestep):", growth_step)
print("\nRESULTS:\n")
print("Time: ", 0, " \tGrowth: ", 0, " \tPopulation: ", 100)
times = np.zeros(int(num_iter)+ 1)
pops = np.zeros(int(num_iter) + 1)
pops[0] = 100

for i in range(1, int(num_iter) + 1):
	growth = growth_step * population
	population = population + growth
	time = i * time_step
	times[i] = time
	pops[i] = population
	print("Time: ", time, " \tGrowth: ", growth, " \tPopulation: ", population)


#Temperatures example
march2017 = np.array([37.7, 29.9, 35.2, 36.1, 36.2, 34.7, 33.8, 34.5, 31.9, 29.9, 30.9, 24.8, 24.2, 24.1, 24.0])
dates = range(1,len(march2017) + 1)
plt.figure(1)
s1 = plt.subplot(311)
s1.set_title("March Temperature")
plt.plot(dates, march2017, "--")
plt.title("March Temperature")
plt.ylabel("Temperature")
plt.xlabel("Date")

s2 = plt.subplot(312)
s2.set_title("March Temperature")
plt.plot(dates, march2017, "ro")
plt.ylabel("Temperature")
plt.xlabel("Date")

s3 = plt.subplot(313)
s3.set_title("March Temperature")
plt.title('Prac3.1: Unconstrained Growth')
plt.plot(times, pops,"r")
plt.show()

