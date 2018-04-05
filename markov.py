import re
import pandas as pd
import datetime as dt
from collections import Counter
ginza = pd.read_csv('ginza_sample_keio.csv')

ginza.columns = ["day","post","devies","etc","etc2","etc3","etc4","etc5"]

def convert_date(day):
	day_mod = re.sub('-','/',day)
	day_mod = re.sub('T06|.***Z',' ',day_mod)
	dt.datetime.strptime(day_mod,'%Y-%m-%d %H:%M:%S')
	return day_mod

#日付を比較して特定の間隔でデータをまとめる
def comparison_date(column,interval):
	base_day = column[0]
	markov = []
	for (index,day) in enumerate(column):
		if day - base_day.day < interval && base_day.devies == day.devies:
		#ここに行列を作成するコードを書く
		markov.append(day.post)
		else:
		#やっぱこっちに書く
		c_markov = Counter(markov)
		
		base_day = day
		markov = []	
			
