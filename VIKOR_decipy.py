# installation (outcomment the line below)
#!pip install decision-python

import numpy as np
import pandas as pd
from decipy import executors as exe

# define matrix
DecisionMatrix = [
    [80, 90, 600],
    [65, 58, 200],
    [83, 60, 400]
]

DecisionMatrix = np.array(DecisionMatrix)

# alternatives
alts = ['A1', 'A2', 'A3']

# criterias
crits = ['C1', 'C2', 'C3']

direction = [False, True, False]

# criteria's weights
weights = [1/3, 1/3, 1/3]

# define DataFrame
xij = pd.DataFrame(DecisionMatrix, index=alts, columns=crits)

# create Executor (MCDM Method implementation)

kwargs = {
    'data': xij,
    'beneficial': direction,
    'weights': weights,
    'rank_reverse': True,
    'rank_method': "ordinal"
}

# Build MCDM Executor
wsm = exe.WSM(**kwargs)  # Weighted Sum Method
topsis = exe.Topsis(**kwargs)  # Topsis
vikor = exe.Vikor(**kwargs)  # Vikor

# show results
print("WSM Ranks")
print(wsm.dataframe)

print("TOPSIS Ranks")
print(topsis.dataframe)

print("Vikor Ranks")
print(vikor.dataframe)

# How to choose best MCDM Method ?

# Instantiate Rank Analizer
comparision_list = exe.RankSimilarityAnalyzer()

# Add MCDMs to anlizer
comparision_list.add_executor(wsm)
comparision_list.add_executor(topsis)
comparision_list.add_executor(vikor)

# run analizer
results = comparision_list.analyze()
print(results)


# Output
'''
WSM Ranks
      RATE  RANK
A1  0.3889   2.0
A2  0.6666   1.0
A3  0.1875   3.0
TOPSIS Ranks
        D+      D-    RATE  RANK
A1  0.1950  0.0871  0.3089   2.0
A2  0.0869  0.1965  0.6933   1.0
A3  0.1712  0.0480  0.2190   3.0
Vikor Ranks
         S       P  RATE  RANK
A1  0.6214  0.3333   NaN   1.0
A2  0.3333  0.3333   NaN   2.0
A3  0.8958  0.3333   NaN   3.0
[0.83333333 0.83333333 0.66666667]
'''
