# Importing necessary libraries
import sys #Used for taking command line arguments
import numpy as np #Used for importing numpy
from pylab import * #Used for plotting and making use of array

#Check for command line arguments
if(len(sys.argv)!=7):
        print "6 arguments have to be passed <n> <M> <nk> <u0> <p> <Msig>"
        exit(1)
else:
        n,M,nk,u0,p,Msig = sys.argv[1:]

#Converting string values into integers and float
n,M,nk,u0,p,Msig = int(n),int(M),int(nk),int(u0),float(p),float(Msig)

#Creating zero vectors 
xx = np.zeros(n*M) #Electron position xx
u = np.zeros(n*M) #Electron velocity u
dx = np.zeros(n*M) #Displacement in current turn dx

I = []# Intensity of emitted light
X = []# Electron position
V = []# Electron Velocity

def insertElectrons(m):
        jj = where(xx==0) #Taking all the values where xx = 0
        jj = jj[0][:m] #Selecting the first m electrons out of it
        xx[jj] = 1 #Assigning those indices as 1
        
def updateValues(ii):
        dx[ii[0]] = u[ii[0]] + 0.5 #Accelerating the dx
        xx[ii[0]] = xx[ii[0]] + dx[ii] #Incrementing the xx
        u[ii[0]] = u[ii[0]] + 1 #Incrementing the velocity
        
def removeElectrons(bb):
        xx[bb[0]] = 0 #Making it's position 0
        dx[bb[0]] = 0 #Making it's dx 0
        u[bb[0]] = 0 #Making it's velocity 0

def simulateCollision(kk):
        if(size(kk[0])>0):
                ll=where(rand(len(kk[0]))<=p)
                kl=kk[0][ll]
                if (size(kl)>0):
                        u[kl] = 0 #Assigning velocity back to 0
                        xx[kl] = xx[kl] - ( dx[kl] * rand(size(kl)) ) #Reducing the position
                        I.extend(xx[kl].tolist()) #Appending to Intensity list

#Iterating nk times
for i in range(nk):
        m = (randn() * Msig) + M #Inserting m electrons everytime
        m = int(m)
        insertElectrons(m)
        ii = where(xx>0) #Checking for where xx>0 and taking in the indices
        X.extend(xx[ii[0]].tolist()) #Adding those position to electron position list
        V.extend(u[ii[0]].tolist()) #Adding those position to electron velocity list
        updateValues(ii)
        bb = where(xx>n) #Checking for if the electron has crossed the tube length
        removeElectrons(bb)
        kk = where(u>u0) #Checking for where the velocity has crossed the threshold velocity
        simulateCollision(kk)

#Function to display the Position Histogram

figure(0)
hist(X, n,(0,n))
xlabel("Position")
ylabel("Electron Density")
title("Population Plot of X")

#Function to display the Intensity Histogram
figure(1)
count = hist(I, n,(0,n))
xlabel("Position")
ylabel("Population count/intensity")
title("Histogram of the light intensity")

#Tabulating the Intensity Plot
print "INTENSITY DATA:"
print "-------------"
print "xpos | count"
print "-------------"
for i in range(len(count[0])):
        print "%d    |    %d" %(count[1][i]+1,count[0][i])

#Function to display the Electron Phase Space Plot
figure(2)
plot(X,V,'ro')
xlabel("Position")
ylabel("Velocity")
title("Electron Phase Space")

show()

