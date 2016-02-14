from pylab import *
import numpy
from scipy.special import jv
from scipy.integrate import quad
def f(t=0.0):
        return 1.0/(1.0+t*t)
def trap(f,su,b,h):
        return h/2.0*(2*su[b]-1.0-su[b]+su[b-1])
x=linspace(0,5,51)
plot(x,f(x),'g',lw=2,label='$1/(1+t^{2})$')
title(r'Plot of $1/(1+t^{2})$')
xlabel('t')
ylabel('$1/(1+t^{2})$')
figure()
y=[]
for i in x:
        y.append(quad(f,0,i)[0])
plot(x,y,'ro',markersize=8,label=r'quad fn')
plot(x,numpy.arctan(x),'black',lw=2,label=r'$\tan^{-1}(x)$')
legend()
title('Plot')
xlabel('x')
ylabel(r'$\int_{0}^{x}du/(1+u^{2})$')
figure()
plot(x,abs(y-numpy.arctan(x)),'ro',markersize=8,label=r'Error in $\int_{0}^{x}du/(1+u^{2})$')
yscale('log')
title(r'Error in $\int_{0}^{x}du/(1+u^{2})$')
ylabel('Error')
xlabel('x')
figure()
n=10
e=1
a=10**-8
z=[]
abserr=[]
eserr=[]
zprev=[]
harr=[]
while(e>a):
        xt=linspace(0,5,5*n+1)
        h=1.0/n
        harr.append(h)
        cum=cumsum(f(xt))
        z=[0]
        for q in range(1,len(cum)):
                z.append(trap(f,cum,q,h))
        if zprev!=[]:
                e=amax(abs(numpy.array(z[::n/10])-zprev[::n/20]))
                eserr.append(e)
        abserr.append(amax(abs(z[::n/10]-numpy.arctan(xt[::n/10]))))
        n*=2
        zprev=z
plot(numpy.array(harr[:-1]),numpy.array(abserr[:-1]),'ro',label='Exact error')
plot(numpy.array(harr[:-1]),numpy.array(eserr),'g+',label='Estimated error')
xscale('log')
yscale('log')
ylabel('Error')
xlabel('h')
legend()
show()
