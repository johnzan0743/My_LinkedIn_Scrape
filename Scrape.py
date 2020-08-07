#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:00:04 2020

@author: yuanzhuang
"""

# Scraping
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Scraping():
    def __init__(self, driver):
        driver.implicitly_wait(10)
        self.last_page = driver.find_elements_by_xpath("//li[@data-test-pagination-page-btn]")[-1].text
        self.url = driver.current_url
        try:
            self.last_page = int(self.last_page)
        except ValueError:
            print('last page number is not a valid number')
    
    
    # grab all the urls from page 1 to last page according to the search results
    def get_all_urls(self,driver):
        if self.last_page == 1:
            url_list = [self.url]
            return url_list
        else:
            url_list = [self.url] # first page
            for i in range(1,self.last_page + 1):
                url_list.append(self.url + '&start=' + str(25*(i)))
            
            return url_list
    
    # grab all the job links within one page
    def get_all_links(self,driver,current_url):
        driver.get(current_url)
        driver.implicitly_wait(10)
        print('1')
        # driver.execute_script("window.scrollTo(0,100)")
        element = driver.find_element_by_xpath("//ul[@itemtype='http://schema.org/ItemList']/li[1]/div[1]/div[1]/div[2]/div[1]/a[1]")
        time.sleep(3)
        for i in range(30):
            element.send_keys(Keys.PAGE_DOWN)
        # js="var q=document.documentElement.scrollTop=10000"
        # driver.execute_script(js)
        
        job_elements = driver.find_elements_by_xpath("//ul[@itemtype='http://schema.org/ItemList']/li")
        driver.implicitly_wait(10)
        print('2')
        # page = requests.get(current_url)
        # soup = BeautifulSoup(page.text, 'html.parser')
        # A = soup.findAll('ul', {'itemtype':'http://schema.org/ItemList'})
        job_links = []
        # for element in A:
        #     job_links.append(element.a['href'])
        for element in job_elements:
            temp = element.find_element_by_css_selector('a')            
            job_links.append(temp.get_attribute('href'))
        
        return job_links
        
        
                
                
                
                
                
                
                
                
                
                