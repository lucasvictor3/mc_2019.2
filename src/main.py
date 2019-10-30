import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

def q1():

	raw_dataset = pd.read_csv('../data/enade2017_ufcg.csv')

	dataset = raw_dataset.copy()
    	sns.relplot(x="QE_I08", y="NT_GER", kind="line",ci=None, data=dataset)
        sns.relplot(x="QE_I23", y="NT_GER", kind="line",ci=None, data=dataset)
        plt.show()        

q1()
