import pandas as pd
import time
import random
import wikipedia

def validName(df):
	df = pd.read_csv(df)
	m = 0
	n = 1
	for _ in range(len(df)):
		try:
			print("Processing ...", df.ScientificName[m])
			print(wikipedia.summary(df.ScientificName[m],sentences=2))
			time.sleep(1)
		except:
			print("Connection lost ..., trying again")
			continue
		finally:
			m = n
			n+=1
        
validName(df = '')
