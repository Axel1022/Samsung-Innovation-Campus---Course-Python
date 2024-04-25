import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Read the CSV file into a DataFrame
df_Peru = pd.read_csv("Data_Perú.csv", sep=';')

# Convert object columns to numeric
df_Peru = df_Peru.apply(pd.to_numeric, errors='ignore')

# Gráfico de Línea de la Expectativa de Vida a lo largo del Tiempo
plt.figure(figsize=(10, 6))
plt.plot(df_Peru['An'], df_Peru['Expectativa de vida'], marker='o', linestyle='-')
plt.title('Expectativa de Vida en Perú (2000-2019)')
plt.xlabel('Año')
plt.ylabel('Expectativa de Vida')
plt.grid(True)
plt.show()

# Diagrama de Dispersión entre la Expectativa de Vida y Otras Variables
variables = ['Acceso a Atencion medica (%)', 'Calidad del agua (%)', 'Nutricion (Indice de desnutricion)',
             'Educacion (Tasa de alfabetizacion)', 'Politicas de salud publica (Indice)']
plt.figure(figsize=(15, 10))
for var in variables:
    plt.scatter(df_Peru['Expectativa de vida'], df_Peru[var], label=var)
plt.title('Diagrama de Dispersión entre Expectativa de Vida y Otras Variables')
plt.xlabel('Expectativa de Vida')
plt.ylabel('Valor de Variables')
plt.legend()
plt.grid(True)
plt.show()

# Mapa de Calor de Correlación
correlation_matrix = df_Peru.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor de Correlación')
plt.show()

# Gráfico de Tendencia de las Variables a lo largo del Tiempo
plt.figure(figsize=(12, 8))
for var in variables:
    plt.plot(df_Peru['An'], df_Peru[var], marker='o', linestyle='-', label=var)
plt.title('Tendencia de Variables a lo largo del Tiempo')
plt.xlabel('Año')
plt.ylabel('Valor de Variables')
plt.legend()
plt.grid(True)
plt.show()
