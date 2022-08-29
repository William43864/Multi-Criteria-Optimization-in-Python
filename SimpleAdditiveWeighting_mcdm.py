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

res = mcdm.rank(DecisionMatrix, 
                alt_names=alt_names, 
                n_method="Linear2", 
                w_method="CRITIC", 
                is_benefit_x=direction,
                s_method="SAW")
print(res)

#Output
'''
[('A1', 0.5277237514195846), ('A2', 0.510823688735553), ('A3', 0.17034304335639175)]
'''
