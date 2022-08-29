#installation (outcomment the line below)
#!pip install easymcdm

from EasyMCDM.models.Promethee import Promethee

DecisionMatrix = {
    #  C1      C2     C3
    "A": [23817.0, 201.0, 8.0],
    "B": [25771.0, 195.0, 5.7],
    "C": [25496.0, 195.0, 7.9]
}

weight    = [1/3,    1/3,  1/3]
direction = ["min", "max", "min"]

p = Promethee(data=DecisionMatrix, verbose=False)
res = p.solve(weights=weight, prefs=direction)
print(res)

# Output
'''
{'phi_negative': [('A', 0.6666666666666666), ('B', 1.0), ('C', 1.0)],
 'phi_positive': [('A', 1.3333333333333333), ('B', 0.6666666666666666), ('C', 0.6666666666666666)],
 'phi': [('A', 0.6666666666666666), ('B', -0.33333333333333337), ('C', -0.33333333333333337)],
 'matrix': 'Please run verbose to get the Promethee II matrix!'}
'''