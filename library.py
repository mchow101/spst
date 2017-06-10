__author__ = 'Bhagat'
import random
def mean(x):
    avr=0
    for y in x:
        avr+=y
    try:
        avr/=float(len(x))
    except ZeroDivisionError:
        return None
    return avr
def create_dataset(length, variance, step=2, correlation=False):
    val=1
    ys=[]
    for i in range(length):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation:
            val+=step
        elif correlation:
            val-=step
    xs = [i for i in range(len(ys))]
    return xs, ys
def product(xs,ys):
    product = []
    for x in range(len(xs)):
        product.append(xs[x]*ys[x])
    return product
def subtract(xs,ys):
    sub = []
    for x in range(len(xs)):
        sub.append(xs[x]-ys[x])
    return sub
def square(xs):
    squared = []
    for x in xs:
        squared.append(x**2)
    return squared
