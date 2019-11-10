# coding: utf-8

import pandas as pd
import seaborn as sns;
import matplotlib.pyplot as plt

raw_dataset = pd.read_csv('../data/enade2017_ufcg.csv')
dataset = raw_dataset.copy()


"""
Foi utilizado uma média de cada classificação categórica de renda por 
Aluno. Em seguida, feito a analise, é possivel verificar que os 3 
primeiros cursos, com maiores notas possuem uma boa média salarial, em 
contra partida dos 4 outros cursos, que possuem uma média 
consideravelmente baixa.

"""
def compare_course_and_socioecon():
	di = {21: u'Arquitetura e Urbanismo', # 50 alunos
		  4004: 'C. da Computacao', # 69 alunos
		  5401: 'C. Sociais (Bacharelado)', # 10 alunos
		  702: 'Matematica (Licenciatura)', # 49 alunos
		  1402: 'Fisica (Licensiatura)', # 21 alunos
		  6002: 'Engenharia de Alimentos', #62 alunos
		  3002: 'Geografia (Licenciatura)'} # 116 alunos
		  
	di_2 = {'A': 700.0,
		  'B': 2000.0,
		  'C': 3500.0,
		  'D': 4900.0,
		  'E': 7700.0,
		  'F': 20000.0,
		  'G': 35000.0}

	df = dataset.replace({'CO_GRUPO': di, 'QE_I08': di_2})
	print(df)
	order_of_x = [di[21], di[4004], di[5401], di[702], di[1402], di[6002], di[3002]]
	plt.figure(figsize=(16, 9))
	
	ax = sns.barplot(x='CO_GRUPO', y='QE_I08', data=df, ci=None, order=order_of_x)
	ax.set_xlabel('Curso', fontsize=15, labelpad=15)
	ax.set_ylabel('Renda Familiar', labelpad=15, fontsize=15)
	
	
	plt.tight_layout()
	plt.ylim(30, None)
	plt.show()

compare_course_and_socioecon()
