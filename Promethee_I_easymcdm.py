#installation (outcomment the line below)
#!pip install easymcdm

from EasyMCDM.models.Promethee import Promethee

DecisionMatrix = {
    #      C1  C2  C3
    "A1": [80, 90, 600],
    "A2": [65, 58, 200],
    "A3": [83, 60, 400]
}

weight    = [1/3,    1/3,  1/3]
direction = ["min", "max", "min"]

p = Promethee(data=DecisionMatrix, verbose=False)
res = p.solve(weights=weight, prefs=direction)
print(res)

# Output
'''
{'phi_negative': [('A2', 0.6666666666666666), ('A1', 1.0), ('A3', 1.3333333333333333)], 
 'phi_positive': [('A2', 1.3333333333333333), ('A1', 1.0), ('A3', 0.6666666666666666)], 
 'phi': [('A2', 0.6666666666666666), ('A1', 0.0), ('A3', -0.6666666666666666)], 
 'matrix': 'Please run verbose to get the Promethee II matrix!'}
'''