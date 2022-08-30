#installation (outcomment the line below)
#!pip install easymcdm

from EasyMCDM.models.WeightedSum import WeightedSum

#============================================================================#
#Ensure to credit the original developer:
#Platform: https://github.com/ktafakkori
#Repository: Multi-Criteria-Optimization-in-Python
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

weight = [1/3,    1/3,  1/3]
direction = ["min", "max", "min"]

p = WeightedSum(data=DecisionMatrix, verbose=False)
res = p.solve(pref_indexes=[0, 1, 2], prefs=direction,
              weights=weight, target='min')
print(res)

#Output
'''
[(1, 'A3', 0.47916666666666663), (2, 'A1', 0.27777777777777796), (3, 'A2', 0.0)]
'''
