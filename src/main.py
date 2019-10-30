import pandas as pd

def q1():
	raw_dataset = pd.read_csv('../data/enade2017_ufcg.csv')

	dataset = raw_dataset.copy()
	print(dataset.tail())

q1()
