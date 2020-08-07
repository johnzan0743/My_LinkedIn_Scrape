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
# from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Search_Parameters import search_bar
from Search_Parameters import result_filter
from Job_search import Search
from Log_in import login
import Scrape



driver = webdriver.Chrome('/Users/yuanzhuang/Downloads/chromedriver')
login(driver)


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
job_links = Instance.get_all_links(driver,url_list[1])



















