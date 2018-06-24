import tushare as ts

print(ts.__version__)


df1=ts.get_today_all()


print(df1.to_csv())




df1.to_csv('a00.csv')

#df1.to_json('a00.json',orient='records')