python csv_to_html.py top100.csv top100.html

python csv_to_html.py top100_low_3jlt.csv top100_low_3jlt.html
python csv_to_html.py top100_middle_3jlt.csv top100_middle_3jlt.html

python csv_to_html.py top100_low_all.csv top100_low_all.html
python csv_to_html.py top100_middle_all.csv top100_middle_all.html
python csv_to_html.py top100_high_all.csv top100_high_all.html

cp  top100* /var/lib/tomcat8/webapps/gupiaoapp2/gupiaodata/

