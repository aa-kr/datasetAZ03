import pandas as pd

df = pd.read_csv('cleaned_prices.csv')
print(df)

average_price = df['Цена'].mean()

print(f'Средняя цена: {average_price}')