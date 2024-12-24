import pandas as pd
# Обработка данных в CSV файле
df = pd.read_csv('prices.csv')

# Удаление " ₽/мес." и преобразование в число
df['Price'] = df['Price'].str.replace(' ₽/мес.', '', regex=False).str.replace(' ', '').astype(float)

# Сохранение изменений в новый CSV файл
df.to_csv('processed_prices.csv', index=False)

print("Данные успешно обработаны и сохранены в 'processed_prices.csv'")