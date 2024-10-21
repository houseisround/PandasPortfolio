import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randint(0,9999,size=(10000,4)), columns=list('ABCD'))

print(data)

data_feature = data.rename(columns={"A": "feature_a", "B": "feature_b", "C": "feature_c", "D": "feature_d"})

print(data_feature)

print(data_feature.mean())

print(data_feature.median())

print(data_feature.describe([.25, .5, .75, .95, .99]))

print(data_feature.agg({"min", "max", "median", "mean", "skew", "count"}))



