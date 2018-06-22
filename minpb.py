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


#for example, we can get the follow data of every end of ths past 7 year
#total shi zhi(Total market value TMV)
#gu dong quan yi(book value ,BV)
#get the pb of every end of ths past 7 year
date_history=[]
tmv_history=[]
bv_history=[]
pb_history=[]

one_year_month_number=4
look_years_num=7
look_report_num=4*look_years_num

for y in range(1,look_years_num+1):
	for m in range(0,one_year_month_number):
		temp_year_str=str(this_year-y)
		temp_month_str="%02d"%(12-m*3)
		if temp_month_str=="12":
			temp_day_str="31"
		elif temp_month_str=="03":
			temp_day_str="31"
		else: ##06,09
			temp_day_str="30"		
		temp_date_str="-".join([temp_year_str,temp_month_str,temp_day_str])
		date_history.append(temp_date_str);
	





str_today=time.strftime('%Y-%m-%d',time.localtime(time.time()))




#access file2
'''
input_file2=codecs.open(str_gupiao_history_report_filename, 'r','gb2312')
for line in input_file2:
	print(line)
input_file2.close()
'''
#print("-----")

date_row_n=0
bv_row_n=18

input_file2=codecs.open(str_gupiao_history_report_filename, 'r','gb2312')
k=0

for line in input_file2:
	if (k==date_row_n):
		temp_date_line=line.split(",")
	if (k==bv_row_n):
		temp_bv_line=line.split(",")	
	#bv_history=[]
	k=k+1

#print(temp_date_line)
#print(temp_bv_line)

k=0
for k in range(0,look_report_num):
	tmv_history.append("-")
	bv_history.append("-")	
	pb_history.append("-")
	
	
#print(bv_history)

k=0
col_offset=1
for one_col in temp_bv_line:
	#print("!k=",k)
	if (k>0 and k<look_report_num+1):
		if (k-col_offset==look_report_num):
			break;#wavoid index out of range
		if (date_history[k-col_offset]==temp_date_line[k]):
			bv_history[k-col_offset]=one_col
			#print("debug1",k,col_offset)
		else:
			if (date_history[k]==temp_date_line[k]):
				col_offset=col_offset-1
				bv_history[k-col_offset]=one_col
				#print("debug2",k,col_offset)
	k=k+1
	
input_file2.close()

#print("--date_history")
#print(date_history)
#print("--tmv_history")
#print(tmv_history)
#print("--bv_history")
#print(bv_history)
#print("--pb_history")
#print(pb_history)

#access file1
input_file1=codecs.open(str_gupiao_history_price_filename, 'r','gb2312')

str_input_file1_header=input_file1.readline()
strlist_input_file1_header=str_input_file1_header.split(",")
#print(strlist_input_file1_header)

tmv_col_n=13

prev_dt_tmpline0=time.strptime(str(this_year)+"-01-01","%Y-%m-%d")

#print(prev_dt_tmpline0)

k=0
the_days_after_ipo=0
gupiao_name=""
gupiao_name_col_n=2
for line in input_file1:
	the_days_after_ipo=the_days_after_ipo+1
	tmpline=line.split(",")
	for t in date_history:
		#print(tmpline[0])
		#print(t)
		dt_tmpline0=time.strptime(tmpline[0],"%Y-%m-%d")
		dt_t=time.strptime(t, "%Y-%m-%d")
		if (dt_t<prev_dt_tmpline0 and dt_t>=dt_tmpline0):
			#print(tmpline);
			#print(tmpline[tmv_col_n]);
			tmv_history[k]=tmpline[tmv_col_n];	
			k=k+1
			if gupiao_name=="":
				gupiao_name=tmpline[gupiao_name_col_n]
			if k>=look_report_num:
				break
	if k>=look_report_num:
		break
	prev_dt_tmpline0=dt_tmpline0		

input_file1.close()


k=0
for k in range(0,look_report_num):
	if tmv_history[k]=="-":
		continue
	if bv_history[k]=="-":
		continue
	f_tmv = float(tmv_history[k])
	f_bv = float(bv_history[k])
	if not f_bv==0.0:
		pb_history[k]=f_tmv/10000/f_bv



print("####output reuslt####")
print("today:",str_today)
#print("--date_history")
#print(date_history)
#print("--tmv_history")
#print(tmv_history)
#print("--bv_history")
#print(bv_history)
#print("--pb_history")
#print(pb_history)
print("gu piao name:",gupiao_name)
print("[7 year pb history]")
print("date          pb")
print("----------    ----------")
k=0
for one_item in date_history:
	if pb_history[k]=="-":
		temp_str_pb="%-10s"%"-"
	else:
		temp_str_pb="%-10.03f"%(pb_history[k])
	print("%s    %s"%(one_item,temp_str_pb))
	k=k+1

print("[min pb]")
pb_history_del_null_for_min=[]
k=0
for temppb in pb_history:
	if not temppb=="-":
		pb_history_del_null_for_min.append(temppb)
		k=k+1
if pb_history_del_null_for_min==[]:
	print("[waring,This gupiao has NO history pb for last year!!!!]")
else:
	this_func_result1="%-10.03f"%(min(pb_history_del_null_for_min))
	print(this_func_result1)
print("[after ipo,at least pass the follow number of day]")
this_func_result2="%-10.00f"%(the_days_after_ipo/250*350)
print(this_func_result2)



