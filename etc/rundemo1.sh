cd /home/dc2-user
cd /var/lib/tomcat7/webapps/ROOT 
sudo nohup java -jar /home/dc2-user/demo-1-0.0.1-SNAPSHOT.jar > /tmp/demo1log.txt  2>&1 &
cd /home/dc2-user
