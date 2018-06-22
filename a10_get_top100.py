from operator import itemgetter
import codecs


input_file=codecs.open("a00.csv", 'r','utf-8')

#output_file_sort=codecs.open("a001.csv", 'w+','utf-8')


output_file_top=codecs.open("a10.csv",'w+','utf-8')



table = []
header = input_file.readline() 
#print(header)

pb_col_no=11;

for line in input_file:
	#print(line)
	col = line.split(",")
	#print(col)
	col[pb_col_no] = float(col[pb_col_no])
	#print(col[pb_col_no]);	
	table.append(col)


table_sorted = sorted(table, key=itemgetter(pb_col_no),reverse = True)

'''
output_file_sort.write(header + '\t')
for row in table_sorted:                    
    row = [str(x) for x in row]   
    #print(row);	
    output_file_sort.write("\t".join(row) + '\n')
'''
header_cols=header.split(",")
header_cols[0]="NO"
header=",".join(header_cols);

print(header);
output_file_top.write(header)

for i in range(0,100):
#for i in range(0,len(table_sorted)):
	table_sorted[i][0]=i+1;
	row=table_sorted[i]
	row_allstr=[]
	for x in row:
		row_allstr+=[str(x)]
	a_output_line=",".join(row_allstr)
	print(a_output_line);
	output_file_top.write(a_output_line)
	
input_file.close()
#output_file_sort.close()
output_file_top.close()