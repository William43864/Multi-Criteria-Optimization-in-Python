import pulp as op
import numpy as np
import sys
import matplotlib.pyplot as plt

#============================================================================#
#Ensure to credit the original developer:
#Platform: https://github.com/ktafakkori
#Repository: Multi-Criteria-Optimization-in-Python
#File: AuGMentedEpsilonCONstraintMethod_pulp.py
#Developer: © Keivan Tafakkori 
#Year: 2022
#Month: August
#Day: 30
#Source: https://github.com/ktafakkori/Multi-Criteria-Optimization-in-Python
#============================================================================#

# decision variables
x = {
     0: op.LpVariable("x1",lowBound = 0, upBound = 20),
     1: op.LpVariable("x2",lowBound = 0, upBound = 40),
     }

# a function for calculating the value of objective given the value of decision variables
def obj_val(k, a):
    if k ==0:
        return a[0]
    if k ==1:
        return 3*a[0]+4*a[1]
     
# objective Functions
obj = {
       0: obj_val(0, x),
       1: obj_val(1, x),
       }

# constraints
cons = {
       0: 5*x[0]+4*x[1] <= 200,
       }

# Generating payoff table using lexicographic optimization
payoff=np.zeros([len(obj),len(obj)]);
for k in range(0,len(obj)):
    model = op.LpProblem("Max",op.LpMaximize)
    model += obj[k]
    for i in range(0,len(cons)):
        model += cons[i]
    result = model.solve()
    if op.LpStatus[result] == 'Optimal':
        print(str(op.LpStatus[result])+" ; max value = "+str(op.value(model.objective))+
          " ; x1_opt = "+str(op.value(x[0]))+
          " ; x2_opt = "+str(op.value(x[1])))
        payoff[k,k]= op.value(model.objective);
        kp=k+1;
        model = op.LpProblem("Max",op.LpMaximize)
        while kp<= len(obj)-1:
                model += obj[kp]
                if kp-1>=0:
                    model += obj[kp-1] >= payoff[k,kp-1]
                for i in range(0,len(cons)):
                    model += cons[i]
                result = model.solve()
                if op.LpStatus[result] == 'Optimal':
                    print(str(op.LpStatus[result])+" ; max value = "+str(op.value(model.objective))+
                  " ; x1_opt = "+str(op.value(x[0]))+
                  " ; x2_opt = "+str(op.value(x[1])))
                    payoff[k,kp]= op.value(model.objective)
                    kp += 1     
                else:
                    sys.exit('no optimal solution for mod_payoff')
        kp=0;
        model += obj[k] >= payoff[k,k]
        while kp< k:
            model += obj[kp]
            if kp-1>=0:
                model += obj[kp-1] >= payoff[k,kp-1]
            for i in range(0,len(cons)):
                model += cons[i]
            result = model.solve()
            if op.LpStatus[result] == 'Optimal':
                print(str(op.LpStatus[result])+" ; max value = "+str(op.value(model.objective))+
                  " ; x1_opt = "+str(op.value(x[0]))+
                  " ; x2_opt = "+str(op.value(x[1])))
                payoff[k,kp]= op.value(model.objective)
                kp += 1
            else:
                sys.exit('no optimal solution for mod_payoff')   
           
    else:
        sys.exit('no optimal solution for mod_payoff')

minobj=np.zeros([len(obj),1]);
maxobj=np.zeros([len(obj),1]);
for k in range(0,len(obj)):
        minobj[k] = min(payoff[:,k]);
        maxobj[k] = max(payoff[:,k]);
        
# slack variables
s = {
     1: op.LpVariable("s2",lowBound = 0),
     }


intervals=4;    
lst = np.empty([intervals+1,len(obj)]);
for g in range(0,intervals+1):
    print('grid point no: ', g+1, 'val: ', maxobj[1] - ((g)/intervals)*(maxobj[1]- minobj[1]))
    model = op.LpProblem("Max",op.LpMaximize)
    code = 1/(maxobj[1]-minobj[1]);
    model += obj[0]+1e-3*s[1]*code
    model += obj[1]- s[1] == maxobj[1] - ((g)/intervals)*(maxobj[1]- minobj[1])
    for i in range(0,len(cons)):
        model += cons[i]
    result = model.solve()
    if op.LpStatus[result] == 'Optimal':
        d = [op.value(x[0]), op.value(x[1])];
        for k in range(0,len(obj)):
            lst[g,k]=obj_val(k, d);
    else:
        print('early exit (jump)')
        break
           
plt.scatter(lst[:,0], lst[:,1])
# set axis lables
plt.xlabel("Z1")
plt.ylabel("Z2")
# set chart title
plt.title("Pareto-Optimal Solutions")
plt.show()
