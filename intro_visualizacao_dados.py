from turtle import color
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')

print(df.head().to_string())

# Histograma
plt.hist(df['salario'])
plt.show()

# Histograma - Paramêtros
plt.figure(figsize=(10, 6))
plt.hist(df['salario'],bins=100, color='orange', alpha=0.8)
plt.title('Histograma - Distribuição de salário')
plt.xlabel('Salário')
plt.xticks(ticks=range(0,int(df['salario'].max())+2000, 2000))
plt.ylabel('Frequencia')
plt.grid(True)
plt.show()

# Multiplos Gráficos
plt.figure(figsize=(10,6))
plt.subplot(2, 2, 1)# 2 linhas, 2 Colunas, primeiro gráfico
# Gráfico de Dispersão
plt.scatter(df['salario'], df['salario'])
plt.title('Dispersão Salário e Salário')
plt.xlabel('Salário')
plt.ylabel('Salário')

plt.subplot(1, 2, 2)# 1 linha, 2 colunas, segundo gráfico
plt.scatter(df['salario'], df['anos_experiencia'], color='#ed3a2d',alpha=0.6, s=30)
plt.title('Gráfico de Dispersão Salário Anos de experiencia')
plt.xlabel('Salário')
plt.ylabel('Anos de Experiência')

# Mapa De Calor
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2, 2, 3) # 1 linham, 2 colunas, primeiro gráfico
sns.heatmap(corr , annot=True, cmap='coolwarm')
plt.title('Correlação Salário e Idade')

plt.tight_layout() #Ajustar espaçamentos
plt.show()

