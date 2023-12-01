# ----- pandas et dataframe---

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('titanic3.xls')
# print(data.shape)
# print(data.columns)


# eliminer des colonnes: data.drop
data = data.drop(['name', 'sex', 'sibsp','parch', 'ticket', 'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'], axis=1)
# print(data.head())
# print(data.describe())

# in case we a missing data we can use data.fillna(data['age'].mean()) for ex.(ici on corromp notre data set en ajoutant ds valeurs potentiellement fausses)
# we can drop data using data = dta.dropna(axis=0)(ici on reduit notre data set)
data = data.dropna(axis=0)
# print(data.shape)
# print(data.describe())
# attention les stats ne sont plus correctes car notre data set est plus petit
# on est passe de 38% de survivants a 40... c est 40% des gens dont l age etait correctment renseigne qui ont survecus

# pour identifier qui etait en quelle classe on va utiliser value_counts
# t = data['pclass'].value_counts()
# print(t)
# to add a graph to it

# data['pclass'].value_counts().plot.bar()
# data['age'].hist()
# plt.show()

# pour regrouper dese gens de cet ex. data.groupy(['sex'])
# t = data.groupby(['sex', 'pclass']).mean()
# print(t)

# indexing sur pandas iloc index localisation
# u = data.iloc[0:2, 0:2]
# print(u)

# indexing sur colonne avec loc
# v = data.loc[0:2, ['age', 'sex']]
# print(v)

# ----- exercise-----
data.loc[data['age'] <= 20, 'age'] = 0
data.loc[(data['age'] >20) & (data['age'] <= 30), 'age'] = 1
data.loc[(data['age']>30) & (data['age']<=40), 'age'] = 2
data.loc[data['age'] >40, 'age'] = 3

print(data.head())
print(data['age'].value_counts())
print(data.groupby(['age']).mean())







