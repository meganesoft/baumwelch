import re
import pandas as pd
import datetime as dt
from collections import Counter
import os
from tqdm import tqdm
import datetime

ginza = pd.read_csv("trance_ginza.csv")
ginza.columns = ["index","day","post","devies","etc","etc2","etc3","etc4","etc5"]
#intervalは計算する範囲の時間の間隔
interval =3
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
	return pd.DataFrame(target)

# 日付を比較して特定の間隔でデータをまとめる
def comparison_date(column,interval):
	#DataFrameの最初の行を入れる
	base_day = pd.DataFrame(column[:1])
	print("base_day.devies")
	print(base_day.devies)
	markov = []
	for (index,day) in tqdm(column.iterrows()):
		print("kore")
		print(day)
		print("korekore")
		print(index)
		print("dayo")
		print(base_day.day)

		print("dayo")
		if (base_day.devies == day["devies"]) & ((day["day"] - base_day.day) < datetime.timedelta(days=interval)):
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
	print(type(trance_ginza))
	trance_ginza["day"] = pd.Series(convert_date(ginza["day"]).values.flatten())
	trance_ginza["post"] = ginza["post"]
	trance_ginza["devies"] = ginza["devies"]
	#intervalは時間の間(1時間単位)	
	comparison_date(trance_ginza,interval)
