import re
import pandas as pd
import datetime as dt
from collections import Counter
import os 
ginza = pd.read_csv("trance_ginza.csv")

ginza.columns = ["index","day","post","devies","etc","etc2","etc3","etc4","etc5"]

def convert_date(days):
	for(i,day) in enumerate(days):
		days.loc[i] = re.sub('T',' ',days.loc[i])
		days.loc[i] = re.sub('(\\\\|\....Z)','',days.loc[i])
		days.loc[i] = dt.datetime.strptime(days.loc[i],'%Y-%m-%d %H:%M:%S')
	print(days)
	return days

# 日付を比較して特定の間隔でデータをまとめる
def comparison_date(column,interval):
	base_day = column[0]
	markov = []
	for (index,day) in enumerate(column):
		if day - base_day.day < interval and base_day.devies == day.devies:
		#ここに行列を作成するコードを書く
			markov.append(day.post)
		else:
		#やっぱこっちに書く
			c_markov = Counter(markov)
			df = pd.DataFrame.from_dict(d,orient='index').reset_index()
			writting_date(df,str(index))
			base_day = day
			markov = []	

def writting_date(index,name):
	index.to_csv(name)

if __name__ == '__main__':
	ginza["day"] = convert_date(ginza["day"])
	#print(ginza["day"])
