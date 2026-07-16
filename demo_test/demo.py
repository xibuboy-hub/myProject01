import pandas as pd

df=pd.read_excel('C:/Users/joy_lo/Desktop/CN53_QTCO_Inventory.xlsx',engine='openpyxl')
print(df.iloc[1:10,1:7])