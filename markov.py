import re
import pandas as pd
import datetime as dt
from collections import Counter
import os
from tqdm import tqdm
ginza = pd.read_csv("trance_ginza.csv")
ginza.columns = ["index","day","post","devies","etc","etc2","etc3","etc4","etc5"]

trance_ginza = pd.DataFrame([],columns=['id'])
print(type(trance_ginza))
#データの日付部分を正規表現で抽出し整形、その後Datatimeオブジェクトに変換
def convert_date(days):
	#破壊的挙動を防ぐための配列target
	target = list(range(len(days)))
	for(i,day) in enumerate(tqdm(days)):
		target[i] = re.sub('T',' ',day)
		target[i] = re.sub('(\\\\|\....Z)','',target[i])
		target[i] = dt.datetime.strptime(target[i],'%Y-%m-%d %H:%M:%S')
	return target

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
			print(c_markov)
			#df = pd.DataFrame.from_dict(c_markov,orient='columns').reset_index()
			#writting_date(df,str(index))
			base_day = day
			markov = []	

def writting_date(index,name):
	index.to_csv(name)

if __name__ == '__main__':
	trance_ginza = convert_date(ginza["day"])
	trance_ginza.append(ginza["post"])
	print(trance_ginza)
	trance_ginza['devies'] = ginza['devies']
	
	#intervalは時間の間(1時間単位)	
	comparison_date(trace_ginza,3)
