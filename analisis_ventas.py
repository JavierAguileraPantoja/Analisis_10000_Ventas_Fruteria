import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Proyecto: Analisis de 10,000 ventas - Fruteria
# Autor: Javier Aguilera Pantoja

np.random.seed(42)
n = 10000
productos = np.random.choice(['mango','platano','papaya','fresa','naranja'], n, p=[0.4, 0.25, 0.15, 0.10, 0.10])
kilos = np.random.randint(5, 50, n)
precios = {'mango':35, 'platano':20, 'papaya':28, 'fresa':60, 'naranja':25}

ventas_big = pd.DataFrame({'producto': productos, 'kilos': kilos})
ventas_big['precio'] = ventas_big['producto'].map(precios)
ventas_big['dinero'] = ventas_big['kilos'] * ventas_big['precio']

resumen = ventas_big.groupby('producto')['dinero'].sum().sort_values(ascending=False)
print(resumen)
print(f"\nTotal vendido: ${resumen.sum():,.0f}")
print(f"Producto estrella: {resumen.idxmax()} con {resumen.max()/resumen.sum()*100:.1f}% del total")

resumen.plot(kind='bar', title='10,000 ventas - Donde esta el dinero?')
plt.show()
