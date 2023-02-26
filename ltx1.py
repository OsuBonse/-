import pandas as pd
from openpyxl import load_workbook

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
length = a.shape[0]

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

data = {'Цільове призначення': a1 , 'Кількість угод': a1_1, 'Площа, га': b1, 'Ціна (вартість), грн./га': c1, 'Значення НГО, грн./га': d1}
df = pd.DataFrame(data)

workbook = load_workbook(filename='opus.xlsx')
worksheet = workbook['123']

last_row = worksheet.max_row
while worksheet.cell(row=last_row, column=3).value is None and last_row > 1:
    last_row -= 1

print(last_row)

with pd.ExcelWriter('opus.xlsx') as writer:
    pd.DataFrame([length]).to_excel(writer, sheet_name='123',startrow=last_row)
    df.to_excel(writer, sheet_name='123', index=True,startrow=8,startcol=1)
