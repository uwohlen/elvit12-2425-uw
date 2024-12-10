a=20
b=30

def f(x):
  return x**2+3*x+1

def der_f(x):
  return 2*x+3

fdc = (f(b)-f(a))/(b-a)

print(fdc)

c = (fdc - 3)/2

print(c)