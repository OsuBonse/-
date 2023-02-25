import pandas as pd

df = pd.read_csv('ltx.csv')
df_group = df.groupby(['PurposeOfTheAssignment', 'Koatyy','Price','ValueNGO'], as_index=False)
a = df['PurposeOfTheAssignment'].value_counts().reset_index()
b = df.groupby('PurposeOfTheAssignment')['Koatyy'].sum().sort_values(ascending=False).reset_index()
c = df.groupby('PurposeOfTheAssignment')['Price'].median().sort_values(ascending=False).reset_index()
d = df.groupby('PurposeOfTheAssignment')['ValueNGO'].median().sort_values(ascending=False).reset_index()

a1 = a['index']
a1_1 = a['PurposeOfTheAssignment']
b1 = b['Koatyy']
c1 = c['Price']
d1 = d['ValueNGO']

print('--------------------------')
print(a1)
print('--------------------------')
print(a1_1)
print('--------------------------')
print(b1)
print('--------------------------')
print(c1)
print('--------------------------')
print(d1)
print('--------------------------')

