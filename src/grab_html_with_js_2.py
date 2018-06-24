#pip3 install selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('lang=zh_CN.UTF-8')
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver.get('http://www.baidu.com')
#driver.get('http://www.sse.com.cn/market/stockdata/activity/')
#driver.get('http://www.sse.com.cn/market/sseindex/indexlist/constlist/index.shtml?COMPANY_CODE=000001&INDEX_Code=000001')
driver.get('http://quote.eastmoney.com/sh600837.html')

print (driver.page_source)
fo = open("aaaa1.txt", "wb")
fo.write(driver.page_source.encode())
fo.close()
driver.quit()