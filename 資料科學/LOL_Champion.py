# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:48:14 2020

@author: user
"""
from selenium import webdriver
import requests
import time
import re
import csv



# Setting ChromeDriver and Crawling the data.It will take about 10 seconds.
url = 'https://www.leagueofgraphs.com/champions/builds'
driverPath = '.\chromedriver.exe'
driver =webdriver.Chrome(driverPath)
def crawl():
    driver.get(url)
    time.sleep(2)
    temp = []
    for j in range(2,160):
        img_temp = []
        if j >2:
            if j == 10 or j%16==2 :
                continue
        img = driver.find_element_by_xpath('//*[@id="mainContent"]/div/div/div/table/tbody/tr[{j}]/td[2]/a/div/div[1]/img'.format(j=j)).get_attribute('class')
        img_temp.append(img)
        img_data.append(img_temp)
        print(img,end='\n')
        temp = []
        for i in range(1,7):
            tr_test = driver.find_element_by_xpath('//*[@id="mainContent"]/div/div/div/table/tbody/tr[{j}]/td[{i}]'.format(i=i,j=j)).get_attribute('innerHTML')
            reg = re.compile('<[^>]*>')
            process = reg.sub('',tr_test).replace('\n','').replace(' ','')
            temp.append(process)     
        data.append(temp)
    driver.close()


# split the original data.
def process():
    global data
    for raw in range(len(data)):
        for ele in range(len(data[raw])):
            data[raw][ele] = (data[raw][ele]
                                 .replace('Jungler','')
                                 .replace(',','')
                                 .replace('Top','')
                                 .replace('ADCarry','')
                                 .replace('Mid','')
                                 .replace('Support',''))


# split kda to another list.
def split_kda(kda_list):
    global data
    for i in range(len(kda_list)):
        kda.append(kda_list[i][5].split('/'))
        data[i] = data[i]+kda[i]
        del data[i][5]
        
    
# Craw img data and process
def img_crawl(img):
    global data
    for i in range(len(img)):
        for j in range(len(img[i])):
            reg = re.compile(r'\-\d+\-')
            match = reg.search(img[i][j])
            img_reg = match.group(0).replace('-','')
            img_url = 'http://lolg-cdn.porofessor.gg/img/champion-icons/10.11/36/{img_reg}.png'.format(img_reg=img_reg)
            img[i][j] = img_url
        data[i] = data[i]+img_data[i]
        
        
# Store in csv
# path='.\output.csv'
# def save_data(data):
#     headers = ['rank','Name','popular','win_rate','ban_rate','kda']
#     with open(path,'w',newline='') as output:
#         writer = csv.writer(output)
#         writer.writerow(headers)
#         # for i in range(len(data)):
#         #     for j in range(len(data[i])):
#         #         writer.writerow(data[i][j])
#         #         print(data[i][j])
                
#         for row in data:
#             writer.writerow(row)
                
        
        
def main(): 
    
    crawl()
    process()
    split_kda(data)
    img_crawl(img_data)
if __name__ == '__main__':
     img_data = []
     data = []
     kda = []
     main()
     

