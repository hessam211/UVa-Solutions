import sys
cf = []
global t
global eps, counter
counter = 0
eps = 0.0001

def npv(irr):
    npv = 0
    for i in range(t + 1):
        npv += cf[i] / pow((1 + irr), i)
    return npv

def check(l, r):
    global eps,counter
    counter += 1
    mid = (l + r) / 2
    if counter == 100:
        print("%.2f"%(mid))
        sys.exit()
    temp = npv(mid)
    if abs(temp) <= eps:
        print("%.2f"%(mid))
    if temp > eps and l <= r:
        check(mid, r)
    if temp < -1*eps and l <= r:
        check(l, mid)

t = int(input())
cf = [int(x) for x in input().split()]
#t = cf.pop(0)
check(-0.99, 10000)



