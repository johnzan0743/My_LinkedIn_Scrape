#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 12:23:11 2020

@author: yuanzhuang
"""
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def Search(driver,search_bar,result_filter):
# go to job market
    url_jobs = 'https://www.linkedin.com/jobs/search/'
    driver.get(url_jobs)
    time.sleep(1)
    
    #element = driver.find_element_by_xpath("//div[@class ='nav-search-bar']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")

    WebDriverWait(driver,25).until(EC.visibility_of_all_elements_located)
    element = WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.XPATH,("//div[@class ='nav-search-bar']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"))))
    time.sleep(3)
    
    # Search by keyword and location
    search_keyword = search_bar['keyword']
    location = search_bar['location']
    

    element.send_keys(search_keyword + Keys.SPACE + Keys.TAB)
    time.sleep(3)
    
    element = driver.find_element_by_xpath("//div[@class ='nav-search-bar']/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/input[1]")
    element.send_keys(location + Keys.SPACE)
    time.sleep(3)
    element.send_keys(Keys.TAB + Keys.ENTER)
    time.sleep(3)
    
    
    
    # Refine Search Settings
    #element = driver.find_element_by_xpath("//section[@aria-label='search filters']/div[1]/div[1]/button[1]")
    
    element = WebDriverWait(driver,25).until(EC.visibility_of_element_located((By.XPATH,("//section[@aria-label='search filters']/div[1]/div[1]/button[1]"))))
    element.click()
    time.sleep(2)
    
    # Clear Filters
    for i in range(3):
        try:
            driver.find_element_by_xpath("//button[@date-control-name='all_filters_clear']").click()
            print('Filters Cleared')
            time.sleep(1)
            break
        except:
            continue
    
    WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='date-posted-facet-values']/fieldset[1]/div[1]/ul[1]/li[1]/label[1]")))
    time.sleep(1)
    # Single-Choice: Sort By
    # most recent
    if result_filter['sort_by'] == 'Most recent':
        driver.find_element_by_css_selector("label[for='sortBy-DD']").click()
    
    # most relevant
    elif result_filter['sort_by'] == 'Most relevant':
        driver.find_element_by_css_selector("label[for='sortBy-R']").click()
    time.sleep(1)
    
    # Single-Choice: Date Posted
    if result_filter['date_posted'] == 'Past 24 hours':
        driver.find_element_by_xpath("//div[@id='date-posted-facet-values']/fieldset[1]/div[1]/ul[1]/li[1]/label[1]").click()
        
    elif result_filter['date_posted'] == 'Past Week':
        driver.find_element_by_xpath("//div[@id='date-posted-facet-values']/fieldset[1]/div[1]/ul[1]/li[2]/label[1]").click()
    
    elif result_filter['date_posted'] == 'Past Month':
        driver.find_element_by_xpath("//div[@id='date-posted-facet-values']/fieldset[1]/div[1]/ul[1]/li[3]/label[1]").click()
    
    elif result_filter['date_posted'] == 'Any Time':
        driver.find_element_by_xpath("//div[@id='date-posted-facet-values']/fieldset[1]/div[1]/ul[1]/li[4]/label[1]").click()
    time.sleep(1)
    
    
    # Multiple-Choices: Experience Level
    if 'Default' in result_filter['Experience Level']:
        pass
    else:
        if 'Internship' in result_filter['Experience Level']:
            driver.find_element_by_xpath("//label[@for='experience-1']").click()
        if 'Entry level' in result_filter['Experience Level']:
            driver.find_element_by_xpath("//label[@for='experience-2']").click()
        if 'Associate' in result_filter['Experience Level']:
            driver.find_element_by_xpath("//label[@for='experience-3']").click()
        if 'Mid-Senior level' in result_filter['Experience Level']:
            driver.find_element_by_xpath("//label[@for='experience-4']").click()
        if 'Director' in result_filter['Experience Level']:
            driver.find_element_by_xpath("//label[@for='experience-5']").click()
        if 'Executive' in result_filter['Experience Level']:
            driver.find_element_by_xpath("//label[@for='experience-6']").click()
    time.sleep(1)
        
        
    # Multiple-Choice: Job-Type
    if 'Default' in result_filter['Job_Type']:
        pass
    else:
        if 'Full-time' in result_filter['Job_Type']:
            try:
                driver.find_element_by_xpath("//label[@for='jobType-F']").click()
            except NoSuchElementException:
                print('Cannot find full-time type of job')
                pass
        if 'Contract' in result_filter['Job_Type']:
            try:
                driver.find_element_by_xpath("//label[for='jobType-C']").click()
            except NoSuchElementException:
                print('Cannot find Contract type of job')
                pass
        if 'Part-time' in result_filter['Job_Type']:
            try:
                driver.find_element_by_xpath("//label[@for='jobType-P']").click()
            except NoSuchElementException:
                print('Cannot find Part-time type of job')
                pass
        if 'Internship' in result_filter['Job_Type']:
            try:
                driver.find_element_by_xpath("//label[@for='jobType-I']").click()
            except NoSuchElementException:
                print("Cannot find Internship type of job")
                pass
        if 'Temporary' in result_filter['Job_Type']:
            try:
                driver.find_element_by_xpath("//label[@for='jobType-T']").click()
            except NoSuchElementException:
                print('Cannot find Temporary type of job')
                pass
    time.sleep(1)
        
    # Apply filter
    driver.find_element_by_xpath("//button[@data-control-name='all_filters_apply']").click()
    time.sleep(1)




