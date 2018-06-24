csv_to_html.py top100.csv top100.html

csv_to_html.py top100_low_3jlt.csv top100_low_3jlt.html
csv_to_html.py top100_middle_3jlt.csv top100_middle_3jlt.html

csv_to_html.py top100_low_all.csv top100_low_all.html
csv_to_html.py top100_middle_all.csv top100_middle_all.html
csv_to_html.py top100_high_all.csv top100_high_all.html


copy /y top100* "C:\nginx-1.14.0\html\gupiaodata\"
copy /y top100* "C:\nginx-1.14.0\html\gupiaoapp2\gupiaodata\"