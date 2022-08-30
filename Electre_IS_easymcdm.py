# installation (outcomment the line below)
# !pip install easymcdm

from EasyMCDM.models.Electre import Electre

#============================================================================#
#Ensure to credit the original developer:
#Platform: https://github.com/ktafakkori
#Repository: Multi-Criteria-Optimization-in-Python
#File: Electre_IS_easymcdm.py
#Developer: © Keivan Tafakkori 
#Year: 2022
#Month: August
#Day: 30
#Source: https://github.com/ktafakkori/Multi-Criteria-Optimization-in-Python
#============================================================================#

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
