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
input_file=codecs.open("a10.csv", 'r','utf-8')

print("--debug1")

#output data
output_file=codecs.open("a30.csv",'w+','utf-8')

print("--debug2")



table = []
str_header = input_file.readline()
#print(str_header)
#print(str_header)
str_header = str_header.strip("\r\n")
#print(str_header)
#print(str_header)

code_col_no=1;
name_col_no=2;
turnoverratio_col_no=10
pb_col_no=13;

#result_table=[];

merged_header=[]
str_merged_header=""

merged_line=[]
str_merged_line=""
k=0

print("--debug3")

for str_line in input_file:
	print("--debug4")
	
	#print(line)
	col = str_line.split(",")
	#print(col)
	gupiao_code= str(col[code_col_no])
	print("--before call get_minpb2 for",gupiao_code)
	out_header=[]
	out_line=[]
	minpb2_lib.get_minpb2(gupiao_code,out_header,out_line)
	print("--after call get_minpb2--")
	#print(out_header)
	#print(out_line)
	#print("yuzyuzyuz")
	str_out_header=",".join(out_header)
	if str_merged_header=="":
		print(str_header)
		print(str_out_header)		
		str_merged_header="%s,%s"%(str_header,str_out_header)
		#str_merged_header=str_merged_header+str_out_header
		#print(str_merged_header)
		#print(str_merged_header)
		#print(str_merged_header)
		#print(str_merged_header)
		output_file.write(str_merged_header)
		
		#output_file.write(str_header)
		#output_file.write(",")
		#output_file.write(str_out_header)
		output_file.write("\n")
	
	str_out_line=",".join(out_line)
	str_merged_line=",".join([str_line.strip(),str_out_line])
	output_file.write(str_merged_line)
	output_file.write("\n")
	
	k=k+1
	#if k>1:
	#	break
	
	
	#gupiao_name= str(col[name_col_no])
	#gupiao_turnoverratio = float(col[turnoverratio_col_no])
	#gupiao_pb = float(col[pb_col_no])
	#one_col_of_result_table=[gupiao_code,gupiao_name,gupiao_turnoverratio,gupiao_pb]
	#result_table.append(one_col_of_result_table)
	

#print(result_table);

input_file.close()
output_file.close()
