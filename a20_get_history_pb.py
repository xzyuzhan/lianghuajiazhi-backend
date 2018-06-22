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



#temp for debug test begin
#gupiao_code="600711"
#gupiao_code="600837"
#gupiao_code="600489"
#minpb2_lib.gen_minpb2_and_save(gupiao_code)
#exit()
#temp for debug test end

#input data
input_file=codecs.open("a10.csv", 'r','utf-8')

#output data
#output_file=codecs.open("a20.csv",'w+','utf-8')





table = []
header = input_file.readline() 
#print(header)
code_col_no=1;
name_col_no=2;
turnoverratio_col_no=10
pb_col_no=13;

result_table=[];

for line in input_file:
	#print(line)
	col = line.split(",")
	#print(col)
	gupiao_code= str(col[code_col_no])
	print("--before call gen_minpb2_and_save for",gupiao_code)
	minpb2_lib.gen_minpb2_and_save(gupiao_code)

	print("--after call gen_minpb2_and_save--")

	#gupiao_name= str(col[name_col_no])
	#gupiao_turnoverratio = float(col[turnoverratio_col_no])
	#gupiao_pb = float(col[pb_col_no])
	#one_col_of_result_table=[gupiao_code,gupiao_name,gupiao_turnoverratio,gupiao_pb]
	#result_table.append(one_col_of_result_table)
	

#print(result_table);

input_file.close()
#output_file.close()