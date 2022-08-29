#installation (outcomment the line below)
#!pip install easymcdm

from EasyMCDM.models.Pareto import Pareto

#Developer: @KeivanTafakkori, 29 August 2022

DecisionMatrix = {
    #      C1  C2  C3
    "A1": [80, 90, 600],
    "A2": [65, 58, 200],
    "A3": [83, 60, 400]
}

direction = ["min", "max", "min"]

p = Pareto(data=DecisionMatrix, verbose=False)
res = p.solve(indexes=[0,1,2], prefs=direction)
print(res)

#Output
'''
{'A1': {'Dominated-by': [], 'Strongly-Dominated-by': []}, 
 'A2': {'Dominated-by': [], 'Strongly-Dominated-by': []}, 
 'A3': {'Dominated-by': [], 'Strongly-Dominated-by': []}}
'''