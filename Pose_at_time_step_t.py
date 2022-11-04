# Humayun_Akhtar
# Importing neccessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Defining Parameters
l = 100
B_next = np.zeros(l)
B_prev =np.full(l,1/l)
X = np.arange(100)
iteration = 50 #<-----------------------Change me for number of time steps
Bell_next = np.zeros(l)
Final_Belief_Xt = np.zeros(l)
Move_one_step = 0.8
Move_no_step = 0.05
Move_two_step = 0.1
Move_one_step_back = 0.05
Wrong_measurement_probability = 0.1
Right_measurement_probability = 0.9

def Bell__Xt (B_prev):
    
    for i in range(l):
        Control_prob = np.zeros(l)
        Control_prob[i] = Move_no_step
        Control_prob[i-1] = Move_one_step
        Control_prob[i-2] = Move_two_step
        if i ==99:
            Control_prob[0] = Move_one_step_back
        else:
            Control_prob[i+1] = Move_one_step_back
        Bell_next[i] = np.sum(np.multiply(Control_prob,B_prev))
    return Bell_next

def Belief_Xt(Bell_next):
    
    result = []
    for i in range(l):        
        B_next[i] = Bell_next[i]*Measurement[i]
    sum = np.sum(B_next)
    N_factor = 1/sum
    for i in B_next:
        result.append(i*N_factor)   
    return result      

for i in range(iteration):
    Bel_Xt = Bell__Xt(B_prev)
    Measurement = np.full(l,Wrong_measurement_probability)
    Measurement[(i+1)%100] = Right_measurement_probability
    Final_Belief_Xt = Belief_Xt(Bel_Xt)
    B_prev = Final_Belief_Xt

print(f'The Bel (Xt) after time steps {iteration} is : {Bel_Xt} ')
print(f'The Belief of position of the Robot at time step {iteration} is : {Final_Belief_Xt}')       
# print(Final_Belief_Xt[iteration-1], Final_Belief_Xt[iteration], Final_Belief_Xt[iteration+1])
plt.plot(X,Final_Belief_Xt)
plt.xlabel('Position of Robot Xt (in meters)')
plt.ylabel('Bel(Xt) ')
plt.title(f'Probability Distribution of Belief of position of Robot at Time step = {iteration}')
plt.show()
