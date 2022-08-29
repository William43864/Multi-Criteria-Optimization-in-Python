#installation (outcomment the line below)
#!pip install mcdm

import mcdm

#Developer: @KeivanTafakkori, 29 August 2022

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