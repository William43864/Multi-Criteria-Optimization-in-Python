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
                n_method="Linear3", 
                w_method="EM", 
                is_benefit_x=direction,
                s_method="mTOPSIS")
print(res)

#Output
'''
[('A2', 0.864871099555024), ('A3', 0.5956069871168261), ('A1', 0.5616265327470062)]
'''
