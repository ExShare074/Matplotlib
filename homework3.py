import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv("divanscraper.csv")

# Преобразуем колонку с ценами в числовой формат
df['Цена'] = pd.to_numeric(df['Цена'], errors='coerce')

# Вычисляем среднюю цену
average_price = df['Цена'].mean()
print(f"Средняя цена на диваны: {average_price:.2f} руб.")

# Строим гистограмму
plt.hist(df['Цена'].dropna(), bins=20, edgecolor='k')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (руб.)')
plt.ylabel('Количество')
plt.show()