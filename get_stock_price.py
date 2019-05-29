# -*- coding: utf-8 -*-
##########################################
#程式檔名：get_nod32_serial.py
#程式名稱：截取奇摩股市價格
#程式類別：爬蟲
#製作日期：2019/03/01
##########################################
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
#https無法使用requests.get()；且此網站也會擋urllib.urlopen()，因此改用Selenium

def get_stock_price(stock_id):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    url = r'https://tw.stock.yahoo.com/q/bc?s='  #元大滬深300正2
    #url = r'https://tw.stock.yahoo.com/q/bc?s=2337'   #旺宏
    driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
    url += stock_id
    driver.get(url)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n\n##################\n{}".format(now))
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    #第一次整理
    soup1 = soup.body.center.find('table',{'align':"center"}).tbody.tr.td.table.tbody.tr.td.find('div',{'class':"highcharts-container"}).svg
    #第二次整理
    soup2 = soup1.find_all('g',{'style':""})

    l_title = []
    for item in soup2[16:30]:   #取得title，例如"開盤"、"買價"
        l_title.append(item.text)

    l_index = 0
    for item in soup2[34:48]:
        #顯示格式範例："開盤:23.05"
        print("{0:s}:{1:s}".format(l_title[l_index],item.text))
        l_index += 1
    print('##################')
    driver.close()

def ask_input():
    stock_id = ""
    l_text = "Please input the stcok id you want to query.\
              \nInput exit to leave.\
              \nYour Answer: "
    while stock_id == "":
        stock_id = input(l_text)

    if stock_id == "exit":
        quit()

    return stock_id

p_stock_id = ask_input()
get_stock_price(p_stock_id)
