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

data = []
def craw():
    
    url = 'https://www.leagueofgraphs.com/champions/builds'
    driverPath = '.\chromedriver.exe'
    
    driver =webdriver.Chrome(driverPath)
    driver.get(url)
    time.sleep(2)
    for j in range(2,160):
        if j >2:
            if j == 10 or j%16==2 :
                continue
        temp = []
        for i in range(1,7):
            tr_test = driver.find_element_by_xpath('//*[@id="mainContent"]/div/div/div/table/tbody/tr[{j}]/td[{i}]'.format(i=i,j=j)).get_attribute('innerHTML')
            reg = re.compile('<[^>]*>')
            process = reg.sub('',tr_test).replace('\n','').replace(' ','')
            temp.append(process)
            print(process,end='\n')
        data.append(temp)
    driver.close()
    
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

kda = []
def split_kda(kda_list):
    global data
    for i in range(len(kda_list)):
        kda.append(kda_list[i][5].split('/'))
        data[i] = data[i]+kda[i]
        del data[i][5]


 if __name__ == '__main__':
     craw()
     process()
     split_kda(data)

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
                
                
            
                
# reg_data = []
# for data in x:
#     reg = re.compile('<[^>]*>')
#     process = reg.sub('',data).replace('\n','').replace(' ','')
#     reg_data.append(process)




# 
# //*[@id="mainContent"]/div/div/div/table/tbody/tr[2]/td[2]/a/div/div[1]/img
# //*[@id="mainContent"]/div/div/div/table/tbody/tr[2]/td[3]/progressbar
# //*[@id="mainContent"]/div/div/div/table/tbody/tr[2]/td[4]/progressbar
# //*[@id="mainContent"]/div/div/div/table/tbody/tr[2]/td[5]/progressbar
# //*[@id="mainContent"]/div/div/div/table/tbody/tr[2]/td[6]
