import pandas as pd

csv_data = pd.read_csv('ginza_sample_keio.csv')

csv_data.columns = ["day","post","devies","etc","etc2","etc3","etc4","etc5"]
csv_data = csv_data.sort_values(by=["devies","day"],ascending=True)
csv_data.to_csv("trance_ginza.csv")
