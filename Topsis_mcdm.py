#installation (outcomment the line below)
#!pip install mcdm

import mcdm

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

DecisionMatrix = [
         [80, 90, 600],
         [65, 58, 200],
         [83, 60, 400]
]

alt_names = ["A1", "A2", "A3"]
direction = [False, True, False]

res = mcdm.rank(DecisionMatrix, n_method="Vector", is_benefit_x=direction, s_method="TOPSIS")

print(res)

#Output
'''
[('a2', 0.6790225178016662), ('a3', 0.4090188985805253), ('a1', 0.3238488379935404)]
'''
