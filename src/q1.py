#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns;
import matplotlib.pyplot as plt
                         
raw_dataset = pd.read_csv('../data/enade2017_ufcg.csv')

dataset = raw_dataset.copy()

def renda_total():
	di = {'A': u'até\nR\$ 1.405,50',
		  'B': 'R\$ 1.405,51 a\n R\$ 2.811,00',
		  'C': 'R\$ 2.811,01 a\n R\$ 4.216,50',
		  'D': 'R\$ 4.216,51 a\n R\$ 5.622,00',
		  'E': 'R\$ 5.622,01 a\n R\$ 9.370,00',
		  'F': 'R\$ 9.370,01 a\n R\$ 28.110,00',
		  'G': 'mais de\n R\$ 28.110,00'}
		  
	df = dataset.replace({'QE_I08': di})
	
	ax = sns.barplot(x='QE_I08', y='NT_GER', data=df)
	ax.set(xlabel = u'Renda Total da Família', ylabel = 'Nota Geral')
	
	plt.tight_layout()
	plt.show()
