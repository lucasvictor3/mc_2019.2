# -*- coding: utf-8 -*-
"""
A nota geral do aluno no ENADE é influenciada por características
socioeconômicas do aluno (contidas no questionário do estudante)? (correlação
e/ou regressão)
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
		  'C': 'Separado(a)\njudicialmente\n/\ndivorciado(a)',
		  'D': 'Viúvo(a)',
		  'E': 'Outro'}

	df = dataset.replace({'QE_I01': di})

	plt.figure(figsize=(8, 4))

	ax = sns.barplot(x='QE_I01', y='NT_GER', data=df, ci=None, order=[di['A'],
                     di['B'], di['C'], di['D'], di['E']])
	ax.set_xlabel('Estado civil', fontsize=14, labelpad=20)
	ax.set_ylabel('Nota geral', fontsize=14, labelpad=20)

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

    print('Estado civil ANOVA:\n\tP-Valor: %.16f' % p)

def cor_raca():
	di = {'A': 'Branca',
		  'B': 'Preta',
		  'C': 'Amarela',
		  'D': 'Parda',
		  'E': 'Indígena',
          'F': 'Não quero\ndeclarar'}

	df = dataset.replace({'QE_I02': di})

	plt.figure(figsize=(6, 4))

	ax = sns.barplot(x='QE_I02', y='NT_GER', data=df, ci=None, order=[di['A'],
                     di['B'], di['C'], di['D'], di['E'], di['F']])
	ax.set_xlabel('Cor/raça', fontsize=14, labelpad=20)
	ax.set_ylabel('Nota geral', fontsize=14, labelpad=20)

	plt.tight_layout()
	plt.ylim(30, None)
	plt.show()

def cor_raca_ANOVA():
    df = dataset.pivot(columns='QE_I02',values='NT_GER')
    F, p = stats.f_oneway(df[df['A'].notnull()]['A'],
                          df[df['B'].notnull()]['B'],
                          df[df['C'].notnull()]['C'],
                          df[df['D'].notnull()]['D'],
                          df[df['E'].notnull()]['E'],
                          df[df['F'].notnull()]['F'])

    print('Cor/raça ANOVA:\n\tP-Valor: %.16f' % p)

def escolarizacao_pai():
	di = {'A': 'Nenhuma',
		  'B': '1ª a 4ª série',
		  'C': '5ª a 8ª série',
		  'D': 'Ensino Médio',
		  'E': 'Graduação',
		  'F': 'Pós-graduação'}

	df = dataset.replace({'QE_I04': di})

	plt.figure(figsize=(8, 4))

	ax = sns.barplot(x='QE_I04', y='NT_GER', data=df, ci=None, order=[
					 di['A'], di['B'], di['C'], di['D'], di['E'],
					 di['F']])
	ax.set_xlabel('Escolarização do pai', fontsize=14, labelpad=20)
	ax.set_ylabel('Nota geral', fontsize=14, labelpad=20)

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

    print('Escolarização do pai ANOVA:\n\tP-Valor: %.16f' % p)

def escolarizacao_mae():
	di = {'A': 'Nenhuma',
		  'B': '1ª a 4ª série',
		  'C': '5ª a 8ª série',
		  'D': 'Ensino Médio',
		  'E': 'Graduação',
		  'F': 'Pós-graduação'}

	df = dataset.replace({'QE_I05': di})

	plt.figure(figsize=(8, 4))

	ax = sns.barplot(x='QE_I05', y='NT_GER', data=df, ci=None, order=[
					 di['A'], di['B'], di['C'], di['D'], di['E'],
					 di['F']])
	ax.set_xlabel('Escolarização da mãe', fontsize=14, labelpad=20)
	ax.set_ylabel('Nota geral', fontsize=14, labelpad=20)

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

    print('Escolarização da mãe ANOVA:\n\tP-Valor: %.16f' % p)

def renda_familiar_total():
	di = {'A': 'até\nR\$ 1.405,50',
		  'B': 'R\$1.405,51\na\n R\$2.811,00',
		  'C': 'R\$2.811,01\na\n R\$4.216,50',
		  'D': 'R\$4.216,51\na\n R\$5.622,00',
		  'E': 'R\$5.622,01\na\n R\$9.370,00',
		  'F': 'R\$9.370,01\na\n R\$28.110,00',
		  'G': 'mais de\n R\$28.110,00'}

	df = dataset.replace({'QE_I08': di})

	plt.figure(figsize=(8, 4))

	ax = sns.barplot(x='QE_I08', y='NT_GER', data=df, ci=None, order=[
					 di['A'], di['B'], di['C'], di['D'], di['E'],
					 di['F'], di['G']])
	ax.set_xlabel('Renda familiar total', fontsize=14, labelpad=20)
	ax.set_ylabel('Nota geral', fontsize=14, labelpad=20)

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

    print('Renda familiar total ANOVA:\n\tP-Valor: %.16f' % p)

def com_quantas_pessoas_mora():
	di = {'A': 'Nenhuma',
		  'B': 'Uma',
		  'C': 'Duas',
		  'D': 'Três',
		  'E': 'Quatro',
          'F': 'Cinco',
          'G': 'Seis',
          'H': 'Sete\nou\nmais'}

	df = dataset.replace({'QE_I07': di})

	plt.figure(figsize=(6, 4))

	ax = sns.barplot(x='QE_I07', y='NT_GER', data=df, ci=None, order=[di['A'],
                     di['B'], di['C'], di['D'], di['E'], di['F'], di['G'],
                     di['H']])
	ax.set_xlabel('Com quantas pessoas mora', fontsize=14, labelpad=20)
	ax.set_ylabel('Nota geral', fontsize=14, labelpad=20)

	plt.tight_layout()
	plt.ylim(40, None)
	plt.show()

def com_quantas_pessoas_mora_ANOVA():
    df = dataset.pivot(columns='QE_I07',values='NT_GER')
    F, p = stats.f_oneway(df[df['A'].notnull()]['A'],
                          df[df['B'].notnull()]['B'],
                          df[df['C'].notnull()]['C'],
                          df[df['D'].notnull()]['D'],
                          df[df['E'].notnull()]['E'],
                          df[df['F'].notnull()]['F'],
                          df[df['G'].notnull()]['G'],
                          df[df['H'].notnull()]['H'])

    print('Com quantas pessoas mora ANOVA:\n\tP-Valor: %.16f' % p)

estado_civil()
estado_civil_ANOVA()
cor_raca()
cor_raca_ANOVA()
escolarizacao_pai()
escolarizacao_pai_ANOVA()
escolarizacao_mae()
escolarizacao_mae_ANOVA()
renda_familiar_total()
renda_familiar_total_ANOVA()
com_quantas_pessoas_mora()
com_quantas_pessoas_mora_ANOVA()
