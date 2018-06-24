from operator import itemgetter
import codecs
import urllib
import urllib.request  
import re
#import pandas as pd
#import pymysql
import os
import time
import minpb2_lib
from sys import argv
print("--this is a95--")

print(argv)
print(len(argv))
ask_risk_level=""
ask_kind=""
if len(argv)==0:
	#ask_risk_level="low_risk"
	#ask_kind="3jlt"
	ask_risk_level="all"
	ask_kind="all"
	
	print("notice:gu piao code is not specified,6000837 will be used as default [gu piao code]!")
elif len(argv)==3:
	ask_risk_level=argv[1]
	ask_kind=argv[2]
elif len(argv)==2:
	ask_risk_level=argv[1]
	ask_kind="all"
else:
	print("please use this script as this: show_risk_level [low,middle,all] [3jlt,all]")

print(ask_risk_level,ask_kind)


low_to_middle_risk_threshold=1.1
middle_to_high_risk_threshold=1.5
ask_all_risk_level_flag=0
if ask_risk_level=="low":
	ask_risk_threshold=low_to_middle_risk_threshold
elif  ask_risk_level=="middle":
	ask_risk_threshold=middle_to_high_risk_threshold
else:
	
	ask_all_risk_level_flag=1


ask_all_kind_flag=0

if ask_kind=="3jlt":
	ask_kind="3jlt"
else:
	ask_all_kind_flag=1
	ask_kind="all"

#input data
input_file=codecs.open("a30.csv", 'r','utf-8')

input_file2=codecs.open("3jlt.csv", 'r','gb2312')
#print("--debug1")

#output data
output_file=codecs.open("top100_%s_%s.csv"%(ask_risk_level,ask_kind),'w+','utf-8')

#print("--debug2")

table_3jlt=[]

temp_one_row=[]
gupiaocode_col_n=0
name3jlt_col_n=4


for x in input_file2:
	str_temp_one_row=x.strip()
	temp_one_row=str_temp_one_row.split(",")
	str_gupiaocode=temp_one_row[gupiaocode_col_n]
	str_gupiaocode=str_gupiaocode[0:6]
	temp_one_row[gupiaocode_col_n]=str_gupiaocode
	str_name3jlt=temp_one_row[name3jlt_col_n]
	table_3jlt.append(temp_one_row)

input_file2.close()






input_file2b=codecs.open("3jlt_add_gnlt.csv", 'r','gb2312')

temp_one_row=[]
gupiaocode_col_n=0
name3jlt_col_n=4

for x in input_file2b:
	str_temp_one_row=x.strip()
	temp_one_row=str_temp_one_row.split(",")
	str_gupiaocode=temp_one_row[gupiaocode_col_n]
	str_gupiaocode=str_gupiaocode[0:6]
	temp_one_row[gupiaocode_col_n]=str_gupiaocode
	str_name3jlt=temp_one_row[name3jlt_col_n]
	table_3jlt.append(temp_one_row)

input_file2b.close()













#print(table_3jlt[199][gupiaocode_col_n],table_3jlt[199][name3jlt_col_n])
#exit()

table = []
str_header = input_file.readline()

str_header = str_header.strip()


code_col_no=1;
name_col_no=2;
turnoverratio_col_no=10
pb_col_no=13;
minpb2_col_no=18;
days_after_ipo_col_no=19;

col_name_risk_level="risk_level"
col_name_ratio_of_pb_to_minpb2="pb_vs_minpb2"
col_name_zhi_neng_cang_wei="zncw0"
col_name_3jlt_name="the_3jlt_name"


#result_table=[];

merged_header=[]
str_merged_header=""

merged_line=[]
str_merged_line=""
k=0

#print("--debug3")
print("-----------------reuslt----------------")
#only out the first 100 line
my_k=1
for str_line in input_file:
	#print("--debug4")

	print(str_line)
	col = str_line.split(",")
	#print(col)
	gupiao_code = str(col[code_col_no])
	gupiao_name = str(col[name_col_no])
	gupiao_turnoverratio = float(col[turnoverratio_col_no])
	gupiao_pb = float(col[pb_col_no])
	gupiao_minpb2 = float(col[minpb2_col_no])
	risk_level="high risk"
	ratio_of_pb_to_minpb2=99
	if gupiao_pb>0 and gupiao_minpb2 > 0 :
		ratio_of_pb_to_minpb2 = round(gupiao_pb / gupiao_minpb2,2)
	
	if ratio_of_pb_to_minpb2>middle_to_high_risk_threshold:
		risk_level="high_risk"
	elif ratio_of_pb_to_minpb2>low_to_middle_risk_threshold:
		risk_level="middle_risk"
	else:
		risk_level="low_risk"
	
	str_risk_level=str(risk_level)
	str_ratio_of_pb_to_minpb2=str(ratio_of_pb_to_minpb2)
	
	###zhi neng cang wei 0 begin
	days_after_ipo = int(col[days_after_ipo_col_no])
	gupiao_pb = float(col[pb_col_no])
	gupiao_minpb2 = float(col[minpb2_col_no])
	zhi_neng_cang_wei=0
	max_cang_wei_per_stock=40000
	zhi_neng_cang_wei=max_cang_wei_per_stock-(gupiao_pb-gupiao_minpb2)*5000
	zhi_neng_cang_wei=zhi_neng_cang_wei*(days_after_ipo/2402)
	zhi_neng_cang_wei=zhi_neng_cang_wei/10000
	zhi_neng_cang_wei=round(zhi_neng_cang_wei,1)
	str_zhi_neng_cang_wei=str(zhi_neng_cang_wei)+'w'
	
	###zhi neng cang wei 0 end
	
	
	
	if str_merged_header=="":
		#print(str_header)
		
		#str_merged_header="%s,%s,%s"%(str_header,col_name_risk_level,col_name_ratio_of_pb_to_minpb2)
		str_merged_header="%s,%s,%s,%s,%s"%(col_name_risk_level,col_name_ratio_of_pb_to_minpb2,col_name_3jlt_name,col_name_zhi_neng_cang_wei,str_header)

		output_file.write(str_merged_header)	
		print(str_merged_header)

		output_file.write("\n")
	

	#str_merged_line="%s,%s,%s"%(str_line.strip(),str_risk_level,str_ratio_of_pb_to_minpb2)
	
	seeked_3jltname="-"
	for row_table_3jlt in table_3jlt:
		if gupiao_code==row_table_3jlt[gupiaocode_col_n]:
			seeked_3jltname=row_table_3jlt[name3jlt_col_n]
	
	str_merged_line="%s,%s,%s,%s,%s"%(str_risk_level,str_ratio_of_pb_to_minpb2,seeked_3jltname,str_zhi_neng_cang_wei,str_line.strip())
	
	
	
	
	if  ask_all_risk_level_flag==1 or ratio_of_pb_to_minpb2<=ask_risk_threshold:
				#print("debug 01",ask_all_kind_flag,seeked_3jltname)
				if ask_all_kind_flag==1 or (ask_kind=="3jlt" and (not seeked_3jltname=="-")):
					output_file.write(str_merged_line)
					output_file.write("\n")
					print(str_merged_line)
					
					my_k = my_k + 1
					if my_k > 100:
						break
	
	
	k=k+1
	#if k>1:
	#	break
	
	

	

#print(result_table);

input_file.close()

output_file.close()
