import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv('processed_prices.csv')

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=10, color='skyblue', edgecolor='black')

# Настройка заголовков и меток
plt.title('Гистограмма цен', fontsize=16)
plt.xlabel('Цена (в рублях)', fontsize=14)
plt.ylabel('Количество', fontsize=14)

# Отображение гистограммы
plt.grid(axis='y', alpha=0.75)
plt.show()

