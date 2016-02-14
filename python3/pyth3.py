import numpy as np 
from pylab import *
import matplotlib.pyplot as plt
import scipy.special as sp

matrix = np.loadtxt('fitting.dat')
t = matrix[ : ,0]
data = matrix[ : ,1 : ]
sigma = np.logspace(-1,-3,9)

# to display the graph generated from fitting.dat
plt.figure(0) 
plt.plot(t,data) 
plt.xlabel(r"$t$") 
plt.ylabel(r"$f(t)=g(t)+n(t)$") 
plt.legend(("Data-1","Data-2","Data-3","Data-4","Data-5","Data-6","Data-7","Data-8","Data-9")) 
plt.title(r"Plot of $f(t)$ v/s $t$")

data1 = data[:,0]

def g(t,A,B):
	return (A*sp.jn(2,t)) + ((B)*t)

y = g(t,1.05,-0.105)

# to display the actual plot
plt.figure(1) 
p = plt.plot(t,y,'b-',label = ("True Value")) 
plt.xlabel(r"$t$") 
plt.ylabel(r"$g(t)$") 
plt.legend() 
plt.title(r"Plot of $g(t)$ v/s $t$") 

# to display the error in the function using errobar
plt.figure(2) 
errorbar(t[::5],data1[::5],sigma[0],fmt='ro') 
plt.xlabel(r"$t$") 
plt.ylabel(r"$Error in data$") 
plt.plot(t,y,'k-')
plt.title(r"Plot of $Error$ v/s $t$")  

x = sp.jn(2,t) # defining the x column vector
M = c_[x,t] # Concatanating the x and time column vectors into a matrix of 2 columns

val = np.array([[1.05],[-0.105]]) # Defining the (A0,B0) column matrix

values =  np.mat(M)*np.mat(val) # Matrix multiplication to find the value of g(t)
y2 = np.array(y) # Converting y2 into an array
y2.shape = (len(y),1) # Converting it into a column matrix by changing the shape of the matrix
print y2 - values # Verify that values obtained from the function and matrix multiplication is same

A = np.arange(0.0,2.0,0.1) # A vector
B = np.arange(-0.2,0.0,0.01) # B vector

# Function to calculate the mean square estimation
def meanSquare(data1,t,A,B):
	sum = 0.0
	for i in range(len(data1)):
		sum = sum + (data1[i] - g(t[i],A,B))**2
	return sum/len(data1)

# Creating a 2D matrix assigning all values to 0
epsilon = np.zeros((len(A),len(A)))

# Iterating through the 2D matrix and assinging calculated values of epsilon
for i in range(len(A)):
	epsilon[i] = meanSquare(data1,t,A[i],B)

# to display the contout plot of epsilon
plt.figure(3) # Setting plt to figure 3
plt.contour(A,B,epsilon) # Plotting the contour plot of epsilon
plt.xlabel(r"A Values") # Setting the X-label
plt.ylabel(r"B Values") # Setting the Y-label
plt.title(r"Contour Plot of $\epsilon$") # Setting the title of the graph

a,b = np.linalg.lstsq(M,data)[0] # Calculating the best estimate of a,b using lstsq function from scipy.linalg
errorInA = abs(a-1.05) # Calculating the error in values of A
errorInB = abs(b+0.105) # Calculating the error in the values of B

# to display error estimate
plt.figure(4) # Setting plt to figure 4
plt.plot(sigma,errorInA,'ro',sigma,errorInB,'b+') # Plotting the graph
plt.xlabel(r"Noise $\sigma$") # Setting the X-label
plt.ylabel(r"Error in values") # Setting the Y-label
plt.legend(("Error in values of A","Error in values of B"))
plt.title(r"Plot of error in A and B values") # Setting the title of the graph

# todisplay error estimate in log scale
plt.figure(5) # Setting plt to figure 4
plt.loglog(sigma,errorInA,'ro',sigma,errorInB,'b+')# Plotting the graph
plt.xlabel(r"Noise $\sigma$") # Setting the X-label
plt.ylabel(r"Error in values") # Setting the Y-label
plt.title(r" loglog Plot of error in A and B values") # Setting the title of the graph
plt.legend(("Error in values of A","Error in values of B"))

plt.show() # show() function to display the plot
