import pulp as op

#============================================================================#
#Ensure to credit the original developer:
#Platform: https://github.com/ktafakkori
#Repository: Multi-Criteria-Optimization-in-Python
#File: BestWorstMethod_pulp.py
#Developer: © Keivan Tafakkori 
#Year: 2022
#Month: August
#Day: 30
#Source: https://github.com/ktafakkori/Multi-Criteria-Optimization-in-Python
#============================================================================#

def model(I,B,W,a,b,dispmodel="y",solve="y", dispresult="y"):
    m = op.LpProblem("Best-WorstMultiCriteriaDecisionMakingProblem", op.LpMinimize)
    w = {i: op.LpVariable(f"w{i}", 0,1, op.LpContinuous) for i in I}
    z = op.LpVariable("z", None,None, op.LpContinuous)
    objs = {0: z}
    cons = {0: {j: w[B[0]]-a[j]*w[j] <=z for j in I},
            1: {j: w[B[0]]-a[j]*w[j] >=-z for j in I},
            2: {j: w[j]-b[j]*w[W[0]] <=z for j in I},
            3: {j: w[j]-b[j]*w[W[0]] >=-z for j in I},
            4: {0: sum(w[j] for j in I) == 1}}
    m += objs[0]
    for keys1 in cons:
        for keys2 in cons[keys1]: m += cons[keys1][keys2]
    if dispmodel == "y":
        print("Model --- \n",m)
    if solve == "y":
        result = m.solve(op.PULP_CBC_CMD(timeLimit=None))
        print(op.LpStatus[result])
    if dispresult=="y" and  op.LpStatus[result] =='Optimal':
        print("Objective --- \n", op.value(m.objective))
        print("Decision --- \n", [(variables.name,variables.varValue) for variables in m.variables() if variables.varValue!=0])
        print("Slack --- \n", [(name,constraint.slack) for name, constraint in m.constraints.items() if constraint.slack!=0])
    return m

I = range(5) #Set of criteria
B = [1] #To indicate best criterion
W = [4] #To indicate worst criterion
a = [2, 1, 4, 3, 8] #Compare the best criterion with others
b = [4, 8, 2, 3, 1] #Compare the worst criterion with others
    
m = model(I,B,W,a,b) #Model and solve the problem
