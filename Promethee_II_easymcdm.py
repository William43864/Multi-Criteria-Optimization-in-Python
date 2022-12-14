#installation (outcomment the line below)
#!pip install easymcdm

from EasyMCDM.models.Promethee import Promethee

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

weight    = [1/3,    1/3,  1/3]
direction = ["min", "max", "min"]

p = Promethee(data=DecisionMatrix, verbose=True)
res = p.solve(weights=weight, prefs=direction)
print(res)

# Output
'''
Weights :  [0.3333333333333333, 0.3333333333333333, 0.3333333333333333]
Preferences :  ['min', 'max', 'min']
+----+------+------+------+------+-------+
|    |  A1  |  A2  |  A3  |  ϕ+  |   ϕ   |
+----+------+------+------+------+-------+
| A1 | 0.00 | 0.33 | 0.67 | 1.00 |  0.00 |
| A2 | 0.67 | 0.00 | 0.67 | 1.33 |  0.67 |
| A3 | 0.33 | 0.33 | 0.00 | 0.67 | -0.67 |
| ϕ- | 1.00 | 0.67 | 1.33 |      |       |
+----+------+------+------+------+-------+


Ranking ϕ- :
************
#1 A2 	: 0.67
#2 A1 	: 1.00
#3 A3 	: 1.33


Ranking ϕ+ :
************
#1 A2 	: 1.33
#2 A1 	: 1.00
#3 A3 	: 0.67


Ranking ϕ :
***********
#1 A2 	: 0.67
#2 A1 	: 0.00
#3 A3 	: -0.67


Best ϕ- is  A2  with  0.67
Best ϕ+ is  A2  with  1.33
Best ϕ  is  A2  with  0.67
{'phi_negative': [('A2', 0.6666666666666666), ('A1', 1.0), ('A3', 1.3333333333333333)], 
 'phi_positive': [('A2', 1.3333333333333333), ('A1', 1.0), ('A3', 0.6666666666666666)], 
 'phi': [('A2', 0.6666666666666666), ('A1', 0.0), ('A3', -0.6666666666666666)], 
 'matrix': '+----+------+------+------+------+-------+\n|    |  A1  |  A2  |  A3  |  ϕ+  |   ϕ   |\n+----+------+------+------+------+-------+\n| A1 | 0.00 | 0.33 | 0.67 | 1.00 |  0.00 |\n| A2 | 0.67 | 0.00 | 0.67 | 1.33 |  0.67 |\n| A3 | 0.33 | 0.33 | 0.00 | 0.67 | -0.67 |\n| ϕ- | 1.00 | 0.67 | 1.33 |      |       |\n+----+------+------+------+------+-------+'}'''
