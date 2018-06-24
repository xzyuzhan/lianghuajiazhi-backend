#!/usr/bin/python
# create html table from csv
# Author(s): Chris Trombley <ctroms@gmail.com>
# Version 2 - added css class to all columns except header

import sys
import csv
import codecs

if len(sys.argv) < 3:
	print("Usage: csvToTable.py csv_file html_file")
	exit(1)

# Open the CSV file for reading
reader = csv.reader(codecs.open(sys.argv[1],"r","utf-8"))

# Create the HTML file for output
htmlfile = codecs.open(sys.argv[2],"w+","utf-8")

# initialize rownum variable
rownum = 0


# write <meta> tag
htmlfile.write('<meta charset="UTF-8">')


# write <table> tag
htmlfile.write('<table>')

for row in reader: # Read a single row from the CSV file
	if rownum == 0:
		htmlfile.write('<tr>') # write <tr> tag
		for column in row:
			htmlfile.write('<th>' + column + '</th>') # write header columns
		htmlfile.write('</tr>') # write </tr> tag
	else: # write all other rows
		colnum = 1
		if rownum % 2 == 0:
			htmlfile.write('<tr class="color1">')
		else:
			htmlfile.write('<tr class="color2">')

		for column in row:
			htmlfile.write('<td class="column_' + str(colnum) + '">' + column + '</td>')
			colnum += 1
		htmlfile.write('</tr>')

	rownum += 1

# write </table> tag
htmlfile.write('</table>')
exit(0)