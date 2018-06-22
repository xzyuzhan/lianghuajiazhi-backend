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

print("--this is a30")

#input data
input_file=codecs.open("a30.csv", 'r','utf-8')

#print("--debug1")

#output data
output_file=codecs.open("top100.csv",'w+','utf-8')

#print("--debug2")



table = []
str_header = input_file.readline()

str_header = str_header.strip()


code_col_no=1;
name_col_no=2;
turnoverratio_col_no=10
pb_col_no=13;
minpb2_col_no=18;
middle_risk_threshold=1.1
high_risk_threshold=1.5
col_name_risk_level="risk_level"
col_name_ratio_of_pb_to_minpb2="pb_vs_minpb2"


#result_table=[];

merged_header=[]
str_merged_header=""

merged_line=[]
str_merged_line=""
k=0

#print("--debug3")
print("-----------------reuslt----------------")
for str_line in input_file:
	#print("--debug4")
	
	#print(line)
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
	
	if ratio_of_pb_to_minpb2>high_risk_threshold:
		risk_level="high_risk"
	elif ratio_of_pb_to_minpb2>middle_risk_threshold:
		risk_level="middle_risk"
	else:
		risk_level="low_risk"
	
	str_risk_level=str(risk_level)
	str_ratio_of_pb_to_minpb2=str(ratio_of_pb_to_minpb2)
	
	if str_merged_header=="":
		#print(str_header)
		
		str_merged_header="%s,%s,%s"%(str_header,col_name_risk_level,col_name_ratio_of_pb_to_minpb2)

		output_file.write(str_merged_header)	
		print(str_merged_header)

		output_file.write("\n")
	

	str_merged_line="%s,%s,%s"%(str_line.strip(),str_risk_level,str_ratio_of_pb_to_minpb2)
	output_file.write(str_merged_line)
	output_file.write("\n")
	print(str_merged_line)
	
	k=k+1
	#if k>1:
	#	break
	
	

	

#print(result_table);

input_file.close()
output_file.close()
