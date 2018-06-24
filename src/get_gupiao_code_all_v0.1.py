from operator import itemgetter
import codecs
import urllib
import urllib.request  
import re
import os
import time
import datetime
from sys import argv
import xlrd

#li zi 1:
#http://www.sse.com.cn/market/sseindex/indexlist/constlist/index.shtml?COMPANY_CODE=000001&INDEX_Code=000001
#but can not get gu piao code....

#li zi 2:
#http://www.sse.com.cn/js/common/ssesuggestdata.js
#_t.push({val:"600030",val2:"中信证券",val3:"zxzq"});
#...
#it can use.


#li zi 3
#中证全指 web page
#http://www.csindex.com.cn/zh-CN/indices/index-detail/000985
#000985cons.xls
#http://www.csindex.com.cn/uploads/file/autofile/cons/000985cons.xls
#中证全指由全部A股股票中剔除ST、*ST股票，以及上市时间不足3个月等股票后的剩余股票构成样本股，具有较高的市场代表性。


#li zi 4
#中证A股指数由沪深两市全部A股组成，并剔除暂停上市的A股，指数以自由流通股本加权计算，综合反映A股上市股票价格的整体表现，具有较高的市场代表性，可作为投资标的和业绩评价基准。 
#http://www.csindex.com.cn/zh-CN/indices/index-detail/930903
#www.csindex.com.cn/uploads/file/autofile/cons/930903cons.xls
#it is very good!!!

os_slash=os.sep
datafilepath = os.getcwd() + os_slash +"data"	+os_slash

if not os.path.exists(datafilepath):
	print("this path will be created,for save data",datafilepath);
	os.makedirs(datafilepath)

#url_0="http://www.sse.com.cn/market/sseindex/indexlist/constlist/index.shtml?COMPANY_CODE=000001&INDEX_Code=000001"
#str_gupiao_sz_code_list_filename=datafilepath+"sz_code_list"+".html"
url_0="http://www.sse.com.cn/js/common/ssesuggestdata.js"
str_gupiao_sz_code_list_filename=datafilepath+"sz_gupiaocode_suggestdata"+".js"
print("access:%s,%s"%(url_0,"............."));
urllib.request.urlretrieve(url_0, str_gupiao_sz_code_list_filename)

output_gupiao_code_list=[]


if os.path.exists(str_gupiao_sz_code_list_filename):
	input_gupiao_code_list_file1=codecs.open(str_gupiao_sz_code_list_filename, 'r','utf-8')
	#to seek the line like this:
	#_t.push({val:"600030",val2:"中信证券",val3:"zxzq"});
	str_pattern1="_t.push({val:\""
	str_pattern2="\","
	len_str_pattern1=len(str_pattern1)
	for line in input_gupiao_code_list_file1:
		str_line=line.strip()
		seek_offset1=str_line.find(str_pattern1)
		if (not seek_offset1==-1):
			sub_str1=str_line[seek_offset1+len_str_pattern1:]
			print(sub_str1)
			seek_offset2=sub_str1.find(str_pattern2)
			sub_str2=sub_str1[0:seek_offset2]
			print(sub_str2)
			str_gupiao_code=sub_str2
			print("%s"%(str_gupiao_code))			
			if not len(str_gupiao_code)==6:
				print("in gen_minpb2_and_save() ,error, invalid gu piao code: %s !"%(str_gupiao_code))
				continue	
			if str_gupiao_code[0]=="6":
				print("%s is A gu."%(str_gupiao_code))
				output_gupiao_code_list.append(str_gupiao_code)
			else:
				print("%s is NOT A gu."%(str_gupiao_code))			
		

	input_gupiao_code_list_file1.close()



#http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1747&ZSDM=399106&tab1PAGENO=1&ENCODE=1&TABKEY=tab1
#it is xlsx file 
url_0b="http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1747&ZSDM=399106&tab1PAGENO=1&ENCODE=1&TABKEY=tab1"
str_gupiao_sz_code_list_excel_filename=datafilepath+"sz_gupiaocode_data"+".xlsx"
print("access:%s,%s"%(url_0b,"............."));
urllib.request.urlretrieve(url_0b, str_gupiao_sz_code_list_excel_filename)


data = xlrd.open_workbook(str_gupiao_sz_code_list_excel_filename) # 打开xls文件
table1 = data.sheets()[0] # 打开第一张表
nrows = table1.nrows # 获取表的行数
for i in range(nrows): # 循环逐行打印
	if i == 0: # 跳过第一行
		continue
	print(table1.row_values(i)[:5]) # 取前5列
	str_gupiao_code = table1.row_values(i)[0]
	if str_gupiao_code[0]=="0" or str_gupiao_code[0]=="3":
		print("%s is A gu."%(str_gupiao_code))
		output_gupiao_code_list.append(str_gupiao_code)
	else:
		print("%s is NOT A gu."%(str_gupiao_code))	


print(output_gupiao_code_list)
print(len(output_gupiao_code_list))


str_gupiao_code_list_filename=datafilepath+"gupiao_code_list_beiyong.txt"
fo = open(str_gupiao_code_list_filename, "w")

print("文件名为: ",fo.name)
fo.write("code")
fo.write("\n")
for str_item in output_gupiao_code_list:
	fo.write( str_item )
	fo.write( "\n" )

# 关闭文件
fo.close()



#中证A股
#www.csindex.com.cn/uploads/file/autofile/cons/930903cons.xls
output_gupiao_code_list=[]

url_0c="http://www.csindex.com.cn/uploads/file/autofile/cons/930903cons.xls"
str_gupiao_code_list_excel_filename=datafilepath+"gupiaocode_data"+".xls"
print("access:%s,%s"%(url_0c,"............."));
urllib.request.urlretrieve(url_0c, str_gupiao_code_list_excel_filename)


data = xlrd.open_workbook(str_gupiao_code_list_excel_filename) # 打开xls文件
table1 = data.sheets()[0] # 打开第一张表
nrows = table1.nrows # 获取表的行数
for i in range(nrows): # 循环逐行打印
	if i == 0: # 跳过第一行
		continue
	print(table1.row_values(i)[:6]) # 取前6列
	str_gupiao_code = table1.row_values(i)[4]
	print("%s is A gu."%(str_gupiao_code))
	output_gupiao_code_list.append(str_gupiao_code)



print(output_gupiao_code_list)
print(len(output_gupiao_code_list))


str_gupiao_code_list_filename=datafilepath+"gupiao_code_list.txt"
fo = open(str_gupiao_code_list_filename, "w")

print("文件名为: ",fo.name)
fo.write("code")
fo.write("\n")
for str_item in output_gupiao_code_list:
	fo.write( str_item )
	fo.write( "\n" )

# 关闭文件
fo.close()






	
for str_item in output_gupiao_code_list:
	str_gupiao_code=str_item
	
	if not len(str_gupiao_code)==6:
		print("error, invalid gu piao code: %s !"%(str_gupiao_code))
		break

	if str_gupiao_code[0]=="6":
		shanghai_shenzhen_flag=0
		dwf_link_shanghai_shenzhen_flag="sh"
	else:
		shanghai_shenzhen_flag=1
		dwf_link_shanghai_shenzhen_flag="sz"
	
	url_3="http://quote.eastmoney.com/%s%s.html"%(dwf_link_shanghai_shenzhen_flag,str_gupiao_code)	
	str_gupiao_dcw_filename=datafilepath+str_gupiao_code+"_dcw"+".html"
	print("access:",url_3,".............");
	urllib.request.urlretrieve(url_3, str_gupiao_dcw_filename)
	#time.sleep(0.1)	
	
	str_gupiao_dcw_filename=datafilepath+str_gupiao_code+"_dcw"+".html"
	cur_pb="999"
	if os.path.exists(str_gupiao_dcw_filename):
		input_dcw_file1=codecs.open(str_gupiao_dcw_filename, 'r','gb2312')
		#to seek the line like this:<td>市净率：<span id="gt13_2">1.11</span></td>
		str_pattern1="<span id=\"gt13_2\">"
		str_pattern2="</span>"
		len_str_pattern1=len(str_pattern1)
		for line in input_dcw_file1:
			str_line=line.strip()
			seek_offset1=str_line.find(str_pattern1)
			if (not seek_offset1==-1):
				sub_str1=str_line[seek_offset1+len_str_pattern1:]
				print(sub_str1)
				seek_offset2=sub_str1.find(str_pattern2)
				sub_str2=sub_str1[0:seek_offset2]
				print(sub_str2)
				cur_pb=sub_str2
				float_pb=float(sub_str2)
				break	
		input_dcw_file1.close()
		print("%s pb=%-10.2f"%(str_gupiao_code,float_pb))
		
	str_gupiao_jz_filename=datafilepath+str_gupiao_code+"_jz"+".csv"
	code=str_gupiao_code

	output_file0=codecs.open(str_gupiao_jz_filename,'w+','utf-8')
	output_file0_header=["code","cur_pb"]
	print(output_file0_header)
	str_output_file0_header=",".join(output_file0_header)
	output_file0.write(str_output_file0_header)
	output_file0.write("\n")
	output_file0_line=[code,cur_pb]
	print(output_file0_line)

	output_file0_line_allstr=[]
	for x in output_file0_line:
		output_file0_line_allstr.append(str(x))
		
	str_output_file0_line=",".join(output_file0_line_allstr)
	output_file0.write(str_output_file0_line)
	output_file0.close()

	


