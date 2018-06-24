csv_to_html.py top100.csv top100.html

csv_to_html.py top100_low_3jlt.csv top100_low_3jlt.html
csv_to_html.py top100_middle_3jlt.csv top100_middle_3jlt.html

csv_to_html.py top100_low_all.csv top100_low_all.html
csv_to_html.py top100_middle_all.csv top100_middle_all.html
csv_to_html.py top100_high_all.csv top100_high_all.html

copy /y top100* "C:\Program Files\Apache Software Foundation\Tomcat 9.0\webapps\gupiaoapp2\gupiaodata\"
copy /y top100* "C:\Program Files\Apache Software Foundation\Tomcat 9.0\webapps\ROOT\gupiaodata\"
copy /y top100* "C:\Program Files\Apache Software Foundation\Tomcat 9.0\webapps\gupiaoapp3\gupiaodata\"
copy /y top100* "E:\sts_workdir\restfulapi05-1\gupiaodata\"

