# coding:utf-8
# ========================
# Considerando cursos que tiveram o mesmo conceito no ENADE, os alunos
# compartilham características sócio-econômicas em comum?
# (essa é a pergunta mais trabalhosa para responder e cada grupo deve 
# identificar como fazer isso).
# ========================

#Cursos Conceito 4:
#	Matematica (Licenciatura) 702
#	Pedagogia (Licencisatura) 2001
#	Engenharia Civil 5710
#	Engenharia Mecanica 5902

import pandas as pd
import seaborn as sns;
import matplotlib.pyplot as plt

raw_dataset = pd.read_csv('../data/enade2017_ufcg.csv')
dataset = raw_dataset.copy()

di = {2402: 'Historia (Licenciatura)', 
	  2001: 'Pedagogia (Licencisatura)', 
	  5710: 'Engenharia Civil', 
	  5902: 'Engenharia Mecanica'} 
	  
def plot_piecharts_courses_by_column(course, socioColumn, socioColumnSize):

	
	#QEI08
	di_2 = {'A': 1.0,
		  'B': 2.0,
		  'C': 3.0,
		  'D': 4.0,
		  'E': 5.0,
		  'F': 6.0,
		  'G': 7.0}
		 
	df1 = dataset.replace({'CO_GRUPO': di, socioColumn: di_2})
	
	df1 = df1[['CO_GRUPO', socioColumn]]
	df2 = df1.loc[df1['CO_GRUPO'] == course]
	
	sizes = []
	for i in range(socioColumnSize):
		retorno = df2.loc[df2[socioColumn] == (i+1)]
		sizes.append(len(retorno))
	
	labels = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'
	colors = ['tab:orange','tab:green','tab:red','tab:purple','tab:blue',
				'tab:pink','black','saddlebrown',]
	labels = labels[:socioColumnSize]

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, 
			shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

	plt.show()
	

columns_groups = ['QE_I06','QE_I07','QE_I08','QE_I09','QE_I10']
size_of_column_group = [6, 8, 7, 6, 5]
#Historia
for i in range(5):
	plot_piecharts_courses_by_column(di[2402], columns_groups[i],
										size_of_column_group[i])
"""
#Pedagogia (Licencisatura)
for i in range(5):
	plot_piecharts_courses_by_column(di[2001], columns_groups[i],
										size_of_column_group[i])

#Engenharia Civil
for i in range(5):
	plot_piecharts_courses_by_column(di[5710], columns_groups[i],
										size_of_column_group[i])

#Engenharia Mecanica
for i in range(5):
	plot_piecharts_courses_by_column(di[5902], columns_groups[i],
										size_of_column_group[i])
"""
