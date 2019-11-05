# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import pandas as pd
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt

raw_dataset = pd.read_csv('../data/enade2017_ufcg.csv')

dataset = raw_dataset.copy()

def estado_civil():
	di = {'A': 'Solteiro(a)',
		  'B': 'Casado(a)',
		  'C': 'Separado(a)\njudicialmente/divorciado(a)',
		  'D': u'Viúvo(a)',
		  'E': 'Outro'}

	df = dataset.replace({'QE_I01': di})

	plt.figure(figsize=(12, 8))

	ax = sns.barplot(x='QE_I01', y='NT_GER', data=df, ci=None, order=[di['A'],
                     di['B'], di['C'], di['D'], di['E']])
	ax.set_xlabel('Estado Civil', fontsize=14, labelpad=20)
	ax.set_ylabel('Nota Geral', fontsize=14, labelpad=20)

	plt.tight_layout()
	plt.ylim(30, None)
	plt.show()

def estado_civil_ANOVA():
    df = dataset.pivot(columns='QE_I01',values='NT_GER')
    F, p = stats.f_oneway(df[df['A'].notnull()]['A'],
                          df[df['B'].notnull()]['B'],
                          df[df['C'].notnull()]['C'],
                          df[df['D'].notnull()]['D'],
                          df[df['E'].notnull()]['E'])

    print('Estado Civil ANOVA:\n\tP-Valor: %.16f' % p)

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

def escolarizacao_pai_ANOVA():
    df = dataset.pivot(columns='QE_I04',values='NT_GER')
    F, p = stats.f_oneway(df[df['A'].notnull()]['A'],
                          df[df['B'].notnull()]['B'],
                          df[df['C'].notnull()]['C'],
                          df[df['D'].notnull()]['D'],
                          df[df['E'].notnull()]['E'],
                          df[df['F'].notnull()]['F'])

    print('Escolarização do Pai ANOVA:\n\tP-Valor: %.16f' % p)

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

def escolarizacao_mae_ANOVA():
    df = dataset.pivot(columns='QE_I05',values='NT_GER')
    F, p = stats.f_oneway(df[df['A'].notnull()]['A'],
                          df[df['B'].notnull()]['B'],
                          df[df['C'].notnull()]['C'],
                          df[df['D'].notnull()]['D'],
                          df[df['E'].notnull()]['E'],
                          df[df['F'].notnull()]['F'])

    print('Escolarização da Mãe ANOVA:\n\tP-Valor: %.16f' % p)

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

def renda_familiar_total_ANOVA():
    df = dataset.pivot(columns='QE_I08',values='NT_GER')
    F, p = stats.f_oneway(df[df['A'].notnull()]['A'],
                          df[df['B'].notnull()]['B'],
                          df[df['C'].notnull()]['C'],
                          df[df['D'].notnull()]['D'],
                          df[df['E'].notnull()]['E'],
                          df[df['F'].notnull()]['F'],
                          df[df['G'].notnull()]['G'])

    print('Renda Familiar Total ANOVA:\n\tP-Valor: %.16f' % p)

def onde_com_quem_mora():
	di = {'A': 'Casa ou apartamento\nsozinho',
		  'B': 'Casa ou apartamento\ncom pais e/ou parentes',
		  'C': 'Casa ou apartamento\ncom cônjuge e/ou filhos',
		  'D': 'Casa ou apartamento\ncom outras pessoas\n(incluindo república)\
',
		  'E': 'Em alojamento\nuniversitário da\nprópria instituição',
          'F': 'Em outros tipos de\nhabitação individual\nou coletiva\n(hotel,\
 hospedaria,\npensão ou outro)'}

	df = dataset.replace({'QE_I06': di})

	plt.figure(figsize=(12, 8))

	ax = sns.barplot(x='QE_I06', y='NT_GER', data=df, ci=None, order=[di['A'],
                     di['B'], di['C'], di['D'], di['E'], di['F']])
	ax.set_xlabel('Onde e com quem Mora', fontsize=14, labelpad=20)
	ax.set_ylabel('Nota Geral', fontsize=14, labelpad=20)

	plt.tight_layout()
	plt.ylim(40, None)
	plt.show()

def onde_com_quem_mora_ANOVA():
    df = dataset.pivot(columns='QE_I06',values='NT_GER')
    F, p = stats.f_oneway(df[df['A'].notnull()]['A'],
                          df[df['B'].notnull()]['B'],
                          df[df['C'].notnull()]['C'],
                          df[df['D'].notnull()]['D'],
                          df[df['E'].notnull()]['E'],
                          df[df['F'].notnull()]['F'])

    print('Onde e com Quem Mora ANOVA:\n\tP-Valor: %.16f' % p)

estado_civil()
estado_civil_ANOVA()
escolarizacao_pai()
escolarizacao_pai_ANOVA()
escolarizacao_mae()
escolarizacao_mae_ANOVA()
onde_com_quem_mora()
onde_com_quem_mora_ANOVA()
renda_familiar_total()
renda_familiar_total_ANOVA()
