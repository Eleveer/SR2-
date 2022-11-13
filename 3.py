import math
start = float(input())
stop = float(input())+1
step = float(input())
for x in range(int(start*10), int(stop*10), int(step*10)):
    x = x/10
    y = ((x-1)//(x**2 - 5*x + 6)) + ((2*x + 1)**(1/3))
    print(y)
