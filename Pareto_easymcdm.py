#installation (outcomment the line below)
#!pip install easymcdm

from EasyMCDM.models.Pareto import Pareto

'''
Copyright (c) 2022, Keivan Tafakkori & FELOOP (https://ktafakkori.github.io)
All rights reserved. Please read the "LICENSE" file for license terms.
Project Code: FELOOP-MOP
Project Title: Multi Criteria Optimization in Python
Publisher: FELOOP (https://ktafakkori.github.io)
Developer: Keivan Tafakkori (Founder of FELOOP)
Cite as:
Tafakkori, K. "Multi Criteria Optimization in Python" (URL: https://github.com/ktafakkori/Multi-Criteria-Optimization-in-Python), FELOOP, 2022.
'''

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
