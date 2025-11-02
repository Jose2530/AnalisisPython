import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

uri_data = 'Phyton/DATOS.xlsx'
df = pd.read_excel(uri_data)
print(df.head())

print('####################DATOS DEMOGRAFICOS###########')
genero = df['GENERO'].tolist() 
print(genero)
edad = df['EDAD'].tolist() 
estado_civil = df['ESTADO_CIVIL'].tolist() 
hijos = df['HIJOS'].tolist() 
nivel_educativo = df['NIVEL_EDUCATIVO'].tolist() 
personas_hogar = df['PERSONAS_HOGAR'].tolist() 
personas_edad_trabajar = df['PERSONAS_EDAD_TRABAJAR'].tolist() 
numero_personas_edad_trabajar = df['NUMERO_PERSONAS_EDAD_TRABAJAR'].tolist() 

print('*****************DATOS ECONOMICOS***************')
ingresos = df['INGRESO'].tolist() 
gastos = df['GASTOS'].tolist() 
vivienda = df['VIVIENDA'].tolist() 

print('!!!!!!!!!!!!!DATOS SOBRE TRANSPORTE!!!!!!!!!!!!')
calilficacion_servicio_trasporte = df['CALIFICACION_SERVICIO_TRANSPORTE'].tolist() 
tiempo_recorrido = df['TIEMPO_RECORRIDO'].tolist() 
gasto_diario_transporte = df['GASTO_DIARIO_TRANSPORTE'].tolist() 

print('!!!!!!!!!!!!!DATOS SOBRE SALUD!!!!!!!!!!!!')
peso_despues_dieta = df['PESO_DESPUES_DIETA'].tolist() 



print('1.) Con base a las edades en la muestra, determine: media, mediana, moda,rango, percentiles 25, 50 y 75#############')
mediana = df["EDAD"].median()
print("Mediana:", mediana)
moda = df["EDAD"].mode()[0]
print("Moda:", moda)
rango = df["EDAD"].max() - df["EDAD"].min()
print("Rango:", rango)
percentil_50 = df["EDAD"].quantile(0.5)
print("Percentil 50:", percentil_50)
percentil_25 = df["EDAD"].quantile(0.25)
print("Percentil 25:", percentil_25)
percentil_75 = df["EDAD"].quantile(0.75)  
print("Percentil 75:", percentil_75)


print('2.) Para los ingresos de los participantes, determine la media, desviasión estandar, histograma y box-plot.#############')

media = df["INGRESO"].mean()
print("La media de INGRESO es:", media)

desviacion = df['INGRESO'].std()
print("Desviación estándar:", desviacion)
plt.hist(df['INGRESO'], bins=10, color="skyblue", edgecolor="black")
plt.title("Histograma de Ingresos")
plt.xlabel("INGRESOS")
plt.ylabel("Frecuencia")
plt.show()

sns.boxplot(x=df['INGRESO'], color="lightgreen")
plt.title("Box-plot de ingresos")
plt.xlabel('INGRESO')
plt.show()

print(df['INGRESO'].describe())

print('3.) Para los gastos mensuales entre los participantes, determine la media, desviasión estandar, histograma y box-plot.#############')

media = df["GASTOS"].mean()
print("La media de GASTOS es:", media)

desviacion = df['GASTOS'].std()
print("Desviación estándar:", desviacion)
plt.hist(df['GASTOS'], bins=10, color="skyblue", edgecolor="black")
plt.title("Histograma de Gatos")
plt.xlabel("GASTOS")
plt.ylabel("Frecuencia")
plt.show()

sns.boxplot(x=df['GASTOS'], color="lightgreen")
plt.title("Box-plot de Gastos")
plt.xlabel('GASTOS')
plt.show()

print(df['GASTOS'].describe())

print('4.) ¿Cuál es la proporción de hombres y mujeres en la muestra? Realice el diagrama de barras y de sectores.#############')


conteoGenero = df['GENERO'].value_counts()
print(conteoGenero)
plt.figure(figsize=(5,5))
plt.pie(
    conteoGenero, 
    labels=conteoGenero.index, 
    autopct='%1.1f%%', 
    startangle=90,
    colors=[ "lightgreen", "salmon"]
)
plt.title("Distribución por Genero")
plt.show()


print('5.) ¿Cuáles son las categorías más comunes en el nivel educativo de la población? Compruébelo a partir de una gráfica de barras.#############')
conteoNivelEducatico = df['NIVEL_EDUCATIVO'].value_counts()
print(conteoNivelEducatico)

plt.figure(figsize=(6, 4))
conteoNivelEducatico.plot(kind='bar', color=['lightgreen', 'skyblue'])
plt.title("Distribución de tipo de vivienda")
plt.xlabel("Tipo de vivienda")
plt.ylabel("Cantidad de personas")
plt.xticks(rotation=0)
plt.show()

print('6.) ¿Qué porcentaje de la población tiene vivienda propia? Realice un gráfico de pastel.#############')
conteoVivienda = df['VIVIENDA'].value_counts()
print(conteoVivienda)

plt.figure(figsize=(6,6))
plt.pie(
    conteoVivienda, 
    labels=conteoVivienda.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=['lightgreen', 'skyblue']
)
plt.title("Distribución de tipo de vivienda")
plt.show()

print('7.) ¿Cuál es la variabilidad en el tiempo de recorrido en transporte público? Determine el Coeficiente de variación.#############')


media =  df['TIEMPO_RECORRIDO'].mean()
desviacion =  df['TIEMPO_RECORRIDO'].std()
cv = (desviacion / media) * 100

print(f"Media: {media:.2f}")
print(f"Desviación estándar: {desviacion:.2f}")
print(f"Coeficiente de variación: {cv:.2f}%")
