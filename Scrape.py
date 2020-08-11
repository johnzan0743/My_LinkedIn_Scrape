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
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from random import random

class Scraping():
    def __init__(self, driver):
        driver.implicitly_wait(10)
        self.last_page = driver.find_elements_by_xpath("//li[@data-test-pagination-page-btn]")[-1].text
        self.url = driver.current_url
        try:
            self.last_page = int(self.last_page)
            self.flag = 1
        except ValueError:
            print('last page number is not a valid number')
            self.flag = 0
    
    
    # grab all the urls from page 1 to last page according to the search results
    def get_all_urls(self,driver):
        if self.flag == 0:
            print('last page number is invalid, no url_list returned')
            url_list = []
            return url_list

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
        time.sleep(1)
        driver.get(current_url)
        # print('1')
        # driver.execute_script("window.scrollTo(0,100)")
        for i in range(10):
            try:
                #element = driver.find_element_by_xpath("//ul[@itemtype='http://schema.org/ItemList']/li[1]/div[1]/div[1]/div[2]/div[1]/a[1]")
                element = WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,"//ul[@itemtype='http://schema.org/ItemList']/li[1]/div[1]/div[1]/div[2]/div[1]/a[1]")))
                break
            except:
                f'Element cannot be loaded or found,try the {i}th time'
        
        for i in range(30):
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(random())
            
        # js="var q=document.documentElement.scrollTop=10000"
        # driver.execute_script(js)
        
        job_elements = driver.find_elements_by_xpath("//ul[@itemtype='http://schema.org/ItemList']/li")
        driver.implicitly_wait(10)
        # print('2')
        original_job_links = []

        for element in job_elements:
            temp = element.find_element_by_css_selector('a')            
            original_job_links.append(temp.get_attribute('href'))
        
        
        job_ids = []
        for job_link in original_job_links:
            try:
                upper_bound = job_link.index('?')
                lower_bound = job_link.index('view')
            except ValueError:
                print('Link is invalid. Cannot find appropriate Job ID')
                job_ids.append(job_link) 
                # if something goes wrong, just append the original job_link
            else:
                job_ids.append(job_link[lower_bound+5:upper_bound-1])
        
        
        shortened_job_links = []
        for job_id in job_ids:
            if job_id.isnumeric():
                shortened_job_links.append('https://www.linkedin.com/jobs/view/' + job_id + '/')
            else:
                shortened_job_links.append(job_id)
                # invalid job id was accquired in the last step, just attch the original link.
            
        return original_job_links, shortened_job_links, job_ids
      
    def get_job_information(self,driver,job_link):
        try:
            response = requests.get(job_link)
        except:
            print('URL is not valid')
            print(job_link)
            return 
        
        
        driver.get(job_link)
        WebDriverWait(driver,25).until(EC.visibility_of_all_elements_located)
        try:
            driver.find_element_by_class_name('error-container')
            print('Job link is wrong or outdated')
            return 
        except:
            pass
                
            
        job_title = driver.find_element_by_tag_name('h1').text
        company_location = driver.find_element_by_xpath("//h3/span[3]").text
        post_time = driver.find_element_by_xpath("//p/span[2]").text
        number_of_applicant = driver.find_element_by_xpath("//p/span[3]/span[2]").text
        
        try:
            driver.find_element_by_xpath("//button[@aria-label='See more']").click()
        except:
            print("No need to expand the job description")
        
    
        
        
                
                
                
                
                
                
                
                
                
                