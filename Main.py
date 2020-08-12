#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:02:33 2020

@author: yuanzhuang
"""

# log in function
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import requests
import re
import time
import json
# from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Search_Parameters import search_bar
from Search_Parameters import result_filter
from Job_search import Search
from Log_in import login
import Scrape


session = requests.Session()
driver = webdriver.Chrome('/Users/yuanzhuang/Downloads/chromedriver')
login(driver)

element = driver.find_element_by_xpath("//input[@placeholder='Search messages']")
if element:
    try:
        driver.find_element_by_xpath("//aside[@id='msg-overlay']/div[1]/header[1]/section[1]/button[1]")
    except:
        print('message-overlay not hidden')
        pass
    


# ---------------------------------------------------- #
# Search the Jobs
Search(driver,search_bar,result_filter)

# If no matching jobs found
try:
    no_job_result = driver.find_element_by_xpath("//div[@class='jobs-search-no-results__image']")
    print('No Matching Jobs Found')
except:
    pass

Instance = Scrape.Scraping(driver)
url_list = Instance.get_all_urls(driver)

# url_list must not be empty
'''
if url_list: 
    for i in range(len(url_list)):
        if i >= 10:
            print('Only the first 10 pages of searched results are studied')
            break
'''
original_job_links, shortened_job_links, job_ids = Instance.get_all_links(driver,url_list[1])

# soup = Instance.get_job_information(driver,shortened_job_links[0])

url = 'https://www.linkedin.com/jobs/view/1880454978/'
soup = Instance.get_job_information(driver,url)
info = {}
if soup:
    temp = soup.find('section',{'class':'show-more-less-html'})
    temp_text = temp.get_text(('\n'))
    temp_text = temp_text.replace('\n \n','\n')
    info['job_description'] = temp_text.replace('\n','\n\n')
    info['job_title'] = soup.find('h2').text
    company_info = soup.findAll('h3',{'class':"topcard__flavor-row"})
    info['company_name'] = company_info[0].select('span')[0].text
    info['company_location'] = company_info[0].select('span')[1].text
    info['post_time'] = company_info[1].select('span')[0].text
    info['current_applicants'] = company_info[1].select('span')[1].text
    job_attributes = soup.find('ul',{'class':'job-criteria__list'}).select('h3')
    job_attributes_li = soup.find('ul',{'class':'job-criteria__list'}).select('li')
    for i in range(len(job_attributes)):
        # info[job_attributes[i].text] = job_attributes_li[i].text
        temp_list = job_attributes_li[i].select('span')
        temp_text = ''
        for temp in temp_list:
            temp_text +=(temp.text + ',\n')
        info[job_attributes[i].text] = temp_text
    
    
    


# if soup:
#     A = soup.findAll('code')
#     temp_dict = json.loads(A[-2].text)
#     code_id = temp_dict['body']
#     js = soup.find('code',{'id':code_id})
#     useful_dict  =json.loads(js.text)
#     company_name = useful_dict['included'][0]['name']
#     company_url = useful_dict['included'][0]['url']
#     job_description = useful_dict['data']['description']['text']
#     company_location = useful_dict['data']['formattedLocation']
#     job_title = useful_dict['data']['title']
    



        
        
    
    



















