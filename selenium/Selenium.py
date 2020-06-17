#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 06:50:55 2020

@author: sakshirathi
"""
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/sakshirathi/Downloads/chromedriver 3')

driver.get('http://kanview.ks.gov/PayRates/PayRates_Agency.aspx')

a = driver.find_element_by_link_text('Adjutant General')
print(a)

a.click()


dataframe = []
for i in range(1):
    link = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(i))
    link.click()
    
    data = BeautifulSoup(driver.page_source,'lxml')
    
    empl = data.table
    
    df = pd.read_html(str(empl),header = 0)
    
    dataframe.append(df[0])
    
    print(dataframe)
