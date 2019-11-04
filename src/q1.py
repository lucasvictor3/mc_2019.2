# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import pandas as pd
import seaborn as sns;
import matplotlib.pyplot as plt

raw_dataset = pd.read_csv('../data/enade2017_ufcg.csv')

dataset = raw_dataset.copy()

def renda_familiar_total():
	di = {'A': u'até\nR\$ 1.405,50',
		  'B': 'R\$ 1.405,51\na\n R\$ 2.811,00',
		  'C': 'R\$ 2.811,01\na\n R\$ 4.216,50',
		  'D': 'R\$ 4.216,51\na\n R\$ 5.622,00',
		  'E': 'R\$ 5.622,01\na\n R\$ 9.370,00',
		  'F': 'R\$ 9.370,01\na\n R\$ 28.110,00',
		  'G': 'mais de\n R\$ 28.110,00'}

	df = dataset.replace({'QE_I08': di})

	plt.figure(figsize=(12, 8))

	ax = sns.barplot(x='QE_I08', y='NT_GER', data=df, ci=None, order=[
					 di['A'], di['B'], di['C'], di['D'], di['E'],
					 di['F'], di['G']])
	ax.set_xlabel('Renda Familiar Total', fontsize=14, labelpad=20)
	ax.set_ylabel('Nota Geral', fontsize=14, labelpad=20)

	plt.tight_layout()
	plt.ylim(40, None)
	plt.show()

def escolarizacao_pai():
	di = {'A': 'Nenhuma',
		  'B': u'Ensino Fundamental:\n1ª a 4ª série',
		  'C': u'Ensino Fundamental:\n5ª a 8ª série',
		  'D': u'Ensino Médio',
		  'E': u'Ensino Superior - Graduação',
		  'F': u'Pós-graduação'}

	df = dataset.replace({'QE_I04': di})

	plt.figure(figsize=(12, 8))

	ax = sns.barplot(x='QE_I04', y='NT_GER', data=df, ci=None, order=[
					 di['A'], di['B'], di['C'], di['D'], di['E'],
					 di['F']])
	ax.set_xlabel(u'Escolarização do Pai', fontsize=14, labelpad=20)
	ax.set_ylabel('Nota Geral', fontsize=14, labelpad=20)

	plt.tight_layout()
	plt.ylim(40, None)
	plt.show()

def escolarizacao_mae():
	di = {'A': 'Nenhuma',
		  'B': u'Ensino Fundamental:\n1ª a 4ª série',
		  'C': u'Ensino Fundamental:\n5ª a 8ª série',
		  'D': u'Ensino Médio',
		  'E': u'Ensino Superior - Graduação',
		  'F': u'Pós-graduação'}

	df = dataset.replace({'QE_I05': di})

	plt.figure(figsize=(12, 8))

	ax = sns.barplot(x='QE_I05', y='NT_GER', data=df, ci=None, order=[
					 di['A'], di['B'], di['C'], di['D'], di['E'],
					 di['F']])
	ax.set_xlabel(u'Escolarização da Mãe', fontsize=14, labelpad=20)
	ax.set_ylabel('Nota Geral', fontsize=14, labelpad=20)

	plt.tight_layout()
	plt.ylim(40, None)
	plt.show()

renda_familiar_total()
escolarizacao_pai()
escolarizacao_mae()
