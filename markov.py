import re
import pandas as pd
import datetime as dt
ginza = pd.read_csv('ginza_sample_keio.csv')

ginza.columns = ["day","post","devies","etc","etc2","etc3","etc4","etc5"]

def convert_date(day):
	day_mod = re.sub('-','/',day)
	day_mod = re.sub('T06|.***Z',' ',day_mod)
	dt.datetime.strptime(day_mod,'%Y-%m-%d %H:%M:%S')
	return day_mod
def comparison_date(column):
	
