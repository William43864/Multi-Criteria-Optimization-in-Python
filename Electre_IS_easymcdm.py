# installation (outcomment the line below)
# !pip install easymcdm

from EasyMCDM.models.Electre import Electre

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

#         C1     C2    C3
weight = [1/3,   1/3,  1/3]
direction = ["min", "max", "min"]
veto = [45,    29,   550]
indifference = 0.6
preference = [20,    10,   200] 

p = Electre(data=DecisionMatrix, verbose=False)
res = p.solve(weight, direction, veto, indifference, preference)
print(res)

# Output
'''
{'kernels': ['A1', 'A2'], 'frequent_kernels': ['A1 (21)', 'A2 (21)', 'A3 (3)']}
'''
