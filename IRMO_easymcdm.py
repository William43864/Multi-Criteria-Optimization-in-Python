#installation (outcomment the line below)
#!pip install easymcdm

from EasyMCDM.models.Irmo import Irmo

DecisionMatrix = {
    #      C1  C2  C3
    "A1": [80, 90, 600],
    "A2": [65, 58, 200],
    "A3": [83, 60, 400]
}

direction = ["min", "max", "min"]

p = Irmo(data=DecisionMatrix, verbose=False)
res = p.solve(
    indexes=[0, 1, 2],
    prefs=direction
)
print(res)

#Output:
'''
{'best': 'A1', 'eleminated': ['A1', 'A2', 'A3']}
'''  