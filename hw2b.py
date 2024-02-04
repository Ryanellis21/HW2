import math
def Secant(fcn, x0, x1, maxiter=10, xtol=1e5):
    iter=0
    while abs(x0-x1)>=xtol and iter<=maxiter:
        x2=x1-(fcn(x1)*(x1-x0))/(fcn(x1)-fcn(x0))
        x0=x1
        x1=x2
        iter+=1
        return x2
def main():
    f1 = lambda x:x-3*math.cos(x)-3
    print('solution of first function:',Secant(f1,1,2,5,1e-4))
    f2= lambda x: math.cos(2*x)*x**3
    print('solution of 1st function:',Secant(f2,1,2,15,1e-8))
    print('Soltion of third function:',Secant(f2,1,2,3,1e-8))

main()