# this program approximates the solution to a first-order linear ODE using Euler's Method
# table and plots adapted from https://github.com/EloneSampaio/Numerical-Methods-First_Order_DE/blob/master/euler_method.py
import math
from matplotlib import pyplot as plt

# step size
delta_t = 0.1

# number of points to plot
n = 100

# initial condition (t0, y0)
t0 = -3
y0 = 2


# slope = dy/dt = f(t, y)
def f(t, y):
	slope = math.sin(y) + t
	return slope


# calculate t values
t = [t0]
t_prev = t0
for i in range(1, n):
	t_next = t_prev + delta_t
	t.append(t_next)
	t_prev = t_next

# calculate y values
y = [y0]
y_prev = y0
for i in range(1, n):
	y_next = y_prev + f(t[i-1], y_prev) * delta_t
	y.append(y_next)
	y_prev = y_next

# print table of values
print("t_n\t    y_n")
for i in range(n):
	print(t[i], "\t", format(y[i], '6f'))

# plot approximation
plt.plot(t, y, '.')
plt.xlabel("Values of t")
plt.ylabel("Values of y")
plt.title("Solution Approximation Using Euler's Method")
plt.show()
