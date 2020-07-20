from math import factorial
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-2,2,0.01) #Independent Variabel Initiation

e_num_pos=0 #For Positive Exponential Expansion In Taylor Series
e_num_neg=0 #For Negative Exponential Expansion In Taylor Series
sin_num=0 #For Sin Expansion In Taylor Series
cos_num=0 #For Cos Expansion In Taylor Series
sign=1

for i in range(0,20):
    e_num_pos=e_num_pos+((x**i)/(factorial(i)))
    e_num_neg=e_num_neg+sign*((x**i)/(factorial(i)))
    sin_num=sin_num+sign*((x**(2*i+1))/(factorial(2*i+1)))
    cos_num=cos_num+sign*((x**(2*i))/(factorial(2*i)))
    sign=-sign

plt.subplot(221)
#plt.title(" Positive Exponential ")
plt.plot(x,e_num_pos,'x',label='Positive Exponential \n Using Taylor Expansion')
plt.plot(x,np.exp(x),label='Positive Exponential \n Using Analytic Method')
plt.legend()
plt.subplot(222)
#plt.title(" Negative Exponential ")
plt.plot(x,e_num_neg,'x',label='Negative Exponential \n Using Taylor Expansion')
plt.plot(x,np.exp(-x),label='Negative Exponential \n Using Analytic Method')
plt.legend()
plt.subplot(223)
plt.plot(x,sin_num,'x',label='Sin Using \n Taylor Expansion')
plt.plot(x,np.sin(x),label='Sin Using \n Analytic Method')
plt.legend()
plt.subplot(224)
plt.plot(x,cos_num,'x',label='Cos Using \n Taylor Expansion')
plt.plot(x,np.cos(x),label='Cos Using \n Taylor Expansion')
plt.legend()
plt.show()
