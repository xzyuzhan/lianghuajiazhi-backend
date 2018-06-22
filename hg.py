from operator import itemgetter
import codecs
import urllib
import urllib.request  
import re
import os
import time
from sys import argv




#test data
str_gupiao_code="600030"
str_gupiao_code="002049"

str_gupiao_code="600362"
str_gupiao_code="002024"
str_gupiao_code="601398"
str_gupiao_code="300024"
str_gupiao_code="600489"
str_gupiao_code="000960"
str_gupiao_code="002024"
str_gupiao_code="000776"
str_gupiao_code="601211"
str_gupiao_code="600547"
str_gupiao_code="600019"
str_gupiao_code="601600"
str_gupiao_code="600219"
str_gupiao_code="601899"
str_gupiao_code="000060"
str_gupiao_code="601989"
str_gupiao_code="601989"
str_gupiao_code="002129"
str_gupiao_code="601088"
str_gupiao_code="002931"
str_gupiao_code="000591"
str_gupiao_code="600837"
str_gupiao_code="603019"


if len(argv)==1:
	str_gupiao_code="600837"
	print("notice:gu piao code is not specified,6000837 will be used as default [gu piao code]!")
else:
	str_gupiao_code=argv[1]
print("An example of a call to this script:")
print("minpb [gu piao code]   #[gu piao code] is an integer such as 600837")
#str_gupiao_code=input()

if str_gupiao_code[0]=="6":
	shanghai_shenzhen_flag=0
else:
	shanghai_shenzhen_flag=1
#print(os.getcwd())
#print(os.getcwd()[:-5])
os_slash=os.sep
datafilepath = os.getcwd() + os_slash +"tempdata"	+os_slash
print("this path will be created,for save data",datafilepath);
if not os.path.exists(datafilepath):
	os.makedirs(datafilepath)


#get data li zi:
#历史成交数据（CSV）：http://quotes.money.163.com/service/chddata.html?code=0601398&start=20000720&end=20150508
#财务指标（CSV）：http://quotes.money.163.com/service/zycwzb_601398.html?type=report



this_year=2018
look_years_num=7
start_year=this_year-look_years_num
end_year=this_year-1
str_start_day="%s0101"%(start_year)
str_end_day="%s1231"%(end_year)



	
print("go to get the gu piao data of %s from %s to %s:"%(str_gupiao_code,str_start_day,str_end_day))
url_1="http://quotes.money.163.com/service/chddata.html?code=%s%s&start=%s&end=%s"%(shanghai_shenzhen_flag,str_gupiao_code,str_start_day,str_end_day)
print("access:",url_1,".............");
url_2="http://quotes.money.163.com/service/zycwzb_%s.html?type=report"%(str_gupiao_code)
print("access:",url_2,".............");





#print("get the data of %s"%str_gupiao_code)
str_gupiao_history_price_filename=datafilepath+str_gupiao_code+"_history_price"+".csv"
urllib.request.urlretrieve(url_1, str_gupiao_history_price_filename)
str_gupiao_history_report_filename=datafilepath+str_gupiao_code+"_history_report"+".csv"
urllib.request.urlretrieve(url_2, str_gupiao_history_report_filename)

url_3="http://quote.eastmoney.com/sh%s.html"%(str_gupiao_code)
print("access:",url_3,".............");
str_gupiao_dcw_filename=datafilepath+str_gupiao_code+"_dcw"+".html"
urllib.request.urlretrieve(url_3, str_gupiao_dcw_filename)



