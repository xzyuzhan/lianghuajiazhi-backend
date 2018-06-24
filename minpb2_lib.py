from operator import itemgetter
import codecs
import urllib
import urllib.request  
import re
import os
import time
import datetime
from sys import argv

def gen_minpb2_and_save(str_gupiao_code):


	#test data
	'''	
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
	'''
	if not len(str_gupiao_code)==6:
		print("in gen_minpb2_and_save() ,error, invalid gu piao code: %s !"%(str_gupiao_code))
		return
	
	if str_gupiao_code[0]=="6":
		shanghai_shenzhen_flag=0
		dwf_link_shanghai_shenzhen_flag="sh"
	else:
		shanghai_shenzhen_flag=1
		dwf_link_shanghai_shenzhen_flag="sz"
	#print(os.getcwd())
	#print(os.getcwd()[:-5])
	os_slash=os.sep
	datafilepath = os.getcwd() + os_slash +"data"	+os_slash
	
	if not os.path.exists(datafilepath):
		print("this path will be created,for save data",datafilepath);
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

	#get dcw data li zi2:
	#http://quote.eastmoney.com/sh600837.html
	#<td>市净率：<span id="gt13_2">1.11</span></td>
    #            <div class="cwzb">
    #                    <table cellpadding="0" cellspacing="0">
    #                        <thead>
    #                            <tr>
    #                                <th>&nbsp;</th>
    #                                <th>总市值</th>
    #                                <th>净资产</th>
    #                                <th>净利润</th>
    #                                <th>市盈率</th>
    #                                <th>市净率</th>
    #                                <th>毛利率</th>
    #                                <th>净利率</th>
    #                                <th>ROE<b title="加权净资产收益率" class="hxsjccsyl"></b></th>
    #                            </tr>
    #                        </thead>
    #                        <tbody>
    #                            <tr>	<td><a href="http://data.eastmoney.com/stockdata/600837.html" target=_blank><b>海通证券</b></a></td>	<td>1303亿</td>	<td>1297亿</td>	<td>86.2亿</td>	<td>15.12</td>	<td>1.11</td>	<td>0.00%</td>	<td>34.99%</td>	<td>7.56%</td></tr><tr>	<td><a href="http://quote.eastmoney.com/center/list.html#28002473_0_2" target="_blank">券商信托</a><br /><b class="color979797">(行业平均)</b></td>	<td>599亿</td>	<td>405亿</td>	<td>26.9亿</td>	<td>44.68</td>	<td>1.73</td>	<td>1.26%</td>	<td>-921.56%</td>	<td>5.83%</td></tr><tr>	<td><b>行业排名</b></td>	<td>3|34</td>	<td>3|34</td>	<td>4|34</td>	<td>5|34</td>	<td>34|34</td>	<td>7|34</td>	<td>13|34</td>	<td>11|34</td></tr><tr>	<td><b>四分位属性</b><b class="showRedTips hxsjccsyl" id="cwzb_sfwsxTit"><div class="sfwsx_title">四分位属性是指根据每个指标的属性，进行数值大小排序，然后分为四等分，每个部分大约包含排名的四分之一。将属性分为高、较高、较低、低四类。<span class="red">注：鼠标移至四分位图标上时，会出现每个指标的说明和用途。</span></div></b></td>	<td>		<ul class="showRedTips">			<li style="background-color:#78b1ff"></li>			<li style="background-color:#a3cbff"></li>			<li style="background-color:#c4ddff"></li>			<li style="border-bottom:none;background-color:#deecff"></li>		</ul>		<p>高</p> <div class="sfwsx_title" style="display: none; margin-left:55px;margin-top:-40px;">公式为公司总股本乘以市价。该指标侧面反映出一家公司的规模和行业地位。总市值越大，公司规模越大，相应的行业地位也越高。<br/><span class="red">注：四分位属性以行业排名为比较基准。</span></div>	</td>	<td>		<ul class="showRedTips">			<li style="background-color:#78b1ff"></li>			<li style="background-color:#a3cbff"></li>			<li style="background-color:#c4ddff"></li>			<li style="border-bottom:none;background-color:#deecff"></li>		</ul>		<p>高</p> <div class="sfwsx_title" style="display: none; margin-left:55px;margin-top:-40px;">公式为资产总额减去负债后的净额。该指标由实收资本、资本公积、盈余公积和未分配利润等构成，反映企业所有者在企业中的财产价值。净资产越大，信用风险越低。<br/><span class="red">注：四分位属性以行业排名为比较基准。</span></div>	</td>	<td>		<ul class="showRedTips">			<li style="background-color:#78b1ff"></li>			<li style="background-color:#a3cbff"></li>			<li style="background-color:#c4ddff"></li>			<li style="border-bottom:none;background-color:#deecff"></li>		</ul>		<p>高</p> <div class="sfwsx_title" style="display: none; margin-left:55px;margin-top:-40px;">公式为：净利润=利润总额-所得税费用。净利润是一个企业经营的最终成果，净利润多，企业的经营效益就好。<br/><span class="red">注：四分位属性以行业排名为比较基准。</span></div>	</td>	<td>		<ul class="showRedTips">			<li></li>			<li></li>			<li></li>			<li style="border-bottom:none;background-color:#deecff"></li>		</ul>		<p>高</p> <div class="sfwsx_title" style="display: none; margin-left:55px;margin-top:-40px;">公式为公司股票价格除以每股利润。该指标主要是衡量公司的价值，高市盈率一般是由高成长支撑着。市盈率越低，股票越便宜，相对投资价值越大。<br/><span class="red">注：四分位属性以行业排名为比较基准。</span></div>	</td>	<td>		<ul class="showRedTips">			<li style="background-color:#78b1ff"></li>			<li style="background-color:#a3cbff"></li>			<li style="background-color:#c4ddff"></li>			<li style="border-bottom:none;background-color:#deecff"></li>		</ul>		<p>低</p> <div class="sfwsx_title" style="display: none; margin-left:55px;margin-top:-40px;">公式为每股股价与每股净资产的比率。市净率越低，每股内含净资产值越高，投资价值越高。<br/><span class="red">注：四分位属性以行业排名为比较基准。</span></div>	</td>	<td>		<ul class="showRedTips">			<li style="background-color:#78b1ff"></li>			<li style="background-color:#a3cbff"></li>			<li style="background-color:#c4ddff"></li>			<li style="border-bottom:none;background-color:#deecff"></li>		</ul>		<p>高</p> <div class="sfwsx_title" style="display: none; margin-left:55px;margin-top:-40px;">公式为毛利与销售收入的比率。毛利率越高，公司产品附加值越高，赚钱效率越高。<br/><span class="red">注：四分位属性以行业排名为比较基准。</span></div>	</td>	<td>		<ul class="showRedTips">			<li></li>			<li style="background-color:#a3cbff"></li>			<li style="background-color:#c4ddff"></li>			<li style="border-bottom:none;background-color:#deecff"></li>		</ul>		<p>较高</p> <div class="sfwsx_title" style="display: none; margin-left:55px;margin-top:-40px;">公式为净利润与主营业务收入的比率。该指标表示企业每单位资产能获得净利润的数量，这一比率越高，说明企业全部资产的盈利能力越强。<br/><span class="red">注：四分位属性以行业排名为比较基准。</span></div>	</td>	<td>		<ul class="showRedTips">			<li></li>			<li style="background-color:#a3cbff"></li>			<li style="background-color:#c4ddff"></li>			<li style="border-bottom:none;background-color:#deecff"></li>		</ul>		<p>较高</p> <div class="sfwsx_title" style="display: none; margin-left:55px;margin-top:-40px;">公式为税后利润与净资产的比率。该指标反映股东权益的收益水平，用以衡量公司运用自有资本的效率。指标值越高，说明投资带来的收益越高。<br/><span class="red">注：四分位属性以行业排名为比较基准。</span></div>	</td></tr>
    #                        </tbody>
    #                    </table>
    #                </div>
	url_3="http://quote.eastmoney.com/%s%s.html"%(dwf_link_shanghai_shenzhen_flag,str_gupiao_code)
	
	str_gupiao_dcw_filename=datafilepath+str_gupiao_code+"_dcw"+".html"
	if os.path.exists(str_gupiao_dcw_filename):
		filedate = os.path.getmtime(str_gupiao_dcw_filename)
		time1 = datetime.datetime.fromtimestamp(filedate).strftime('%Y-%m-%d')
		date1 = time.time()
		#num1 =(date1 - filedate)/60/60
		#if num1 >= 2:#del file 2 hour ago
		#num1 =(date1 - filedate)/60
		#if num1 >= 30:#del file 30 min ago
		try:
			os.remove(str_gupiao_dcw_filename)
			print(u"file %s is removed." %  (str_gupiao_dcw_filename))            
		except Exception as e:                                             
			print(e)
				
	if not os.path.exists(str_gupiao_dcw_filename):
		print("access:",url_3,".............");
		urllib.request.urlretrieve(url_3, str_gupiao_dcw_filename)
		#time.sleep(0.1)
	
	cur_pb="999"
	if os.path.exists(str_gupiao_dcw_filename):
		input_dcw_file1=codecs.open(str_gupiao_dcw_filename, 'r','gbk')#gb2312 -> gbk
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
	
	
	
	##########	
	print("go to get the gu piao data of %s from %s to %s:"%(str_gupiao_code,str_start_day,str_end_day))
	url_1="http://quotes.money.163.com/service/chddata.html?code=%s%s&start=%s&end=%s"%(shanghai_shenzhen_flag,str_gupiao_code,str_start_day,str_end_day)
	
	url_2="http://quotes.money.163.com/service/zycwzb_%s.html?type=report"%(str_gupiao_code)
	


	#print("get the data of %s"%str_gupiao_code)
	str_gupiao_history_price_filename=datafilepath+str_gupiao_code+"_history_price"+".csv"
	if not os.path.exists(str_gupiao_history_price_filename):
		print("access:",url_1,".............");
		urllib.request.urlretrieve(url_1, str_gupiao_history_price_filename)
		time.sleep(0.1)
	
	str_gupiao_history_report_filename=datafilepath+str_gupiao_code+"_history_report"+".csv"
	if not os.path.exists(str_gupiao_history_report_filename):
		print("access:",url_2,".............");
		urllib.request.urlretrieve(url_2, str_gupiao_history_report_filename)
		time.sleep(0.1)
	

	str_gupiao_minpb2_filename=datafilepath+str_gupiao_code+"_minpb2"+".csv"
	
	if not os.path.exists(str_gupiao_minpb2_filename):
		

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
		print("-----")#for trace

		date_row_n=0
		bv_row_n=18

		input_file2=codecs.open(str_gupiao_history_report_filename, 'r','gbk')#try gb2312 -> gbk?
		k=0

		for line in input_file2:
			if (k==date_row_n):
				temp_date_line=line.split(",")
			if (k==bv_row_n):
				temp_bv_line=line.split(",")	
			#bv_history=[]
			k=k+1

		print(temp_date_line)#for trace
		print(temp_bv_line)#for trace

		k=0
		for k in range(0,look_report_num):
			tmv_history.append("-")
			bv_history.append("-")	
			pb_history.append("-")
			
			
		print(bv_history)#for trace


		
		len_of_temp_date_line=len(temp_date_line)
		
		if len_of_temp_date_line<4:
			print("jump gen the minpb of ci xin gu!")#TODO:
			return
		
		k=0
		flag_hit=0
		for one_col in temp_date_line:
			if date_history[0]==one_col:
				flag_hit=1
				break;
			k=k+1
		
		col_offset=0
		if k==1:
			col_offset=1
		if k==2:
			col_offset=2
		if k==3:
			col_offset=3	
		if k==4:
			if flag_hit==1:
				col_offset=4	
		
		k=0
		for one_col in temp_bv_line:
			print("!k=",k)#for trace
			
			if k>0:
				#print("debug1_0",k)#for trace

				
				if k-col_offset>=0 and k-col_offset<look_report_num:
					#print("debug1_1",k,col_offset,look_report_num)#for trace

			
					if col_offset==0:
						bv_history[k-col_offset]=one_col
						print("debug2_0",k,col_offset)#for trace			


					if col_offset==1:
						bv_history[k-col_offset]=one_col
						print("debug2_1",k,col_offset)#for trace
						
						
					if col_offset==2:
						bv_history[k-col_offset]=one_col
						print("debug2_2",k,col_offset)#for trace
						
					if col_offset==3:
						bv_history[k-col_offset]=one_col
						print("debug2_3",k,col_offset)#for trace
						
					if col_offset==4:
						bv_history[k-col_offset]=one_col
						print("debug2_3",k,col_offset)#for trace
			'''			
			if k==1:
				if (date_history[k]==temp_date_line[k]):
					col_offset=0
					bv_history[k+col_offset]=one_col
					print("debug2_0",k,col_offset)#for trace
				elif(date_history[k]==temp_date_line[k-1]):
					col_offset=1
					bv_history[k-col_offset]=one_col
					print("debug2_1",k,col_offset)#for trace
				elif (date_history[k]==temp_date_line[k+2]):
					col_offset=2
					bv_history[k-col_offset]=one_col
					print("debug2_2",k,col_offset)#for trace
				elif (date_history[k]==temp_date_line[k+3]):
					col_offset=3
					bv_history[k-col_offset]=one_col
					print("debug2_3",k,col_offset)#for trace
				else:
					print("debug2_x","invalid file format")#for trace
					break
					
			
			if (k>1 and k<look_report_num+1):
				if (k-col_offset==look_report_num):
					break;#wavoid index out of range
				if (date_history[k-col_offset]==temp_date_line[k]):
					bv_history[k-col_offset]=one_col
					print("debug1",k,col_offset)#for trace
			'''
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
		input_file1=codecs.open(str_gupiao_history_price_filename, 'r','gbk')#try gb2312 -> gbk?

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
			if bv_history[k]=="--":
				continue
			f_bv = float(bv_history[k])
			if not f_bv==0.0:
				pb_history[k]=round(f_tmv/10000/f_bv,3)



		print("####output reuslt####")



		print("today:",str_today)
		print("--date_history")
		print(date_history)
		print("--tmv_history")
		print(tmv_history)
		print("--bv_history")
		print(bv_history)
		print("--pb_history")
		print(pb_history)
		print("gu piao name:",gupiao_name)
		print("[7 year pb history]")
		print("date          pb")
		print("----------    ----------")
		hpb_prefix_date_history=[]
		for one_item in date_history:
			hpb_prefix_date_history.append('pb'+one_item)
		print("--date_history")
		print(hpb_prefix_date_history)
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
		minpb1=0
		minpb2=0
		if pb_history_del_null_for_min==[]:
			print("[waring,This gupiao has NO history pb for last year!!!!]")
		else:
			minpb1=min(pb_history_del_null_for_min)
			minpb2=9999999.999#TODO:need more compute!! ,minpb2 is greater than minpb1 and less than the others pb
			temp_pb=minpb2
			for pb_k in pb_history_del_null_for_min:
				if pb_k>minpb1:
					temp_pb=min(pb_k,temp_pb)
			if temp_pb==9999999.999:
				minpb2=minpb1
			else:
				minpb2=temp_pb
			print("%-10.03f"%(minpb1))
			this_func_result1=minpb2

		print("[after ipo,at least pass the follow number of day]")
		days_after_ipo=int(round(the_days_after_ipo/250*365,0))
		print("%-10d"%(days_after_ipo))
		this_func_result2=days_after_ipo


		code=str_gupiao_code

		output_file=codecs.open(str_gupiao_minpb2_filename,'w+','utf-8')
		output_file_header=["code","minpb1","minpb2","days_after_ipo"]+hpb_prefix_date_history#date_history -> hpb_prefix_date_history
		print(output_file_header)
		str_output_file_header=",".join(output_file_header)
		output_file.write(str_output_file_header)
		output_file.write("\n")
		output_file_line=[code,minpb1,minpb2,days_after_ipo]+pb_history
		print(output_file_line)

		output_file_line_allstr=[]
		for x in output_file_line:
			output_file_line_allstr.append(str(x))
			
		str_output_file_line=",".join(output_file_line_allstr)
		output_file.write(str_output_file_line)
		output_file.close()

	return


	
	
	
	
def get_minpb2(str_gupiao_code,out_header,out_line):
	code=str_gupiao_code

	
	
	os_slash=os.sep
	datafilepath = os.getcwd() + os_slash +"data"	+os_slash

	if not os.path.exists(datafilepath):
		print("in get_minpb2() ,error, data file path %s is not exist!"%(datafilepath))
		return;

	str_gupiao_minpb2_filename=datafilepath+str_gupiao_code+"_minpb2"+".csv"	
	
	if not os.path.exists(str_gupiao_minpb2_filename):
		print("in get_minpb2() ,error, data file for for gu piao code: %s is not exist!"%(str_gupiao_code))
		return;	
	
	input_file=codecs.open(str_gupiao_minpb2_filename,'r','utf-8')
	'''
	output_file_header=["code","minpb1","minpb2","days_after_ipo"]+date_history
	print(output_file_header)
	str_output_file_header=",".join(output_file_header)
	output_file.write(str_output_file_header)
	output_file.write("\n")
	output_file_line=[code,minpb1,minpb2,days_after_ipo]+pb_history
	print(output_file_line)
	'''
	str_header=""
	str_line=""
	str_header=input_file.readline()
	#print(str_header)
	#print(str_header)
	str_header=str_header.strip("\r\n")
	#print(str_header)
	#print(str_header)

	temp_out_header=str_header.split(",")
	print(temp_out_header)

	
	
	print("in get_minpb2()",temp_out_header)
	out_header.extend(temp_out_header)
	
	str_line=input_file.readline()
	str_line=str_line.strip("\r\n")
	
	
	temp_out_line=str_line.split(",");
	print("in get_minpb2()",temp_out_line)
	out_line.extend(temp_out_line)
	'''
	output_file_line_allstr=[]
	for x in output_file_line:
		output_file_line_allstr.append(str(x))
		
	str_output_file_line=",".join(output_file_line_allstr)
	output_file.write(str_output_file_line)
	output_file.close()
	'''

	return