'''Collatz Conjecture
Calculate the sequence and plot a graph to show range of numbers and iterations   '''
import matplotlib.pyplot as plt
import numpy as np
def collatz(z):
    ''' This fun calculates next number in collatz sequence'''
    if z % 2 == 0:
        return z // 2
    elif z % 2 == 1:
        return z * 3 + 1

# Range considered here is 1 to 999 it can be changed and set by taking user input
# Negative nos are not considered
start_pt=1
end_pt=99999
plot_dict=np.zeros(end_pt+1)    # Dictionary to keep count of steps required for each no
hist_dict=np.zeros(1000)

for i in range(start_pt,end_pt+1):
    # this for loop considers one number and starts calculating collatz Conjecture for one number
    number=i
    count=0
    while(number!=1):           # Collatz sequence calculation
        number=collatz(number)
        count+=1
    plot_dict[i]=count      # this will store the no. of conjecture steps at index=input number
    hist_dict[count]+=1

#print(plot_dict)
plot1=plt.figure(1)
plt.plot(plot_dict,'.')
plt.xlabel('Number')
plt.ylabel('No. of steps(iterations)')
plt.title('Iteration time for input numbers')


#print(hist_dict)
# Histogram plot
plot2=plt.figure(2)
plt.plot(hist_dict)
plt.xlabel('No.of steps/ stopping time')
plt.ylabel('Occurance of stopping time')
plt.title('Histogram')
plt.show()
