#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 14:04:20 2020

@author: yuanzhuang
"""
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# one-time only
def login(driver):
    Email = 'xxxxxx@yyy.com'
    Password = 'xxxxxx'
    url = 'https://www.linkedin.com/home'
    

    driver.get(url)
    WebDriverWait(driver,25).until(EC.visibility_of_all_elements_located)
    
    driver.find_element_by_xpath("//input[@id='session_key']").send_keys(Email)
    driver.find_element_by_xpath("//input[@id='session_password']").send_keys(Password)
    driver.find_element_by_xpath("//button[@type='submit']").submit()
    time.sleep(3)
    
    # potential confirmation
    try:
        driver.find_element_by_xpath("//button[@class='primary-action-new']")
    except NoSuchElementException:
        print('No need to confirm the account')
        pass
    
    
    # Disable message overlay panel
    # element = driver.find_element_by_xpath("//aside[@id='msg-overlay']/div[1]/header[1]/section[1]/button[1]")

    try:
        element = WebDriverWait(driver,25).until(EC.element_to_be_clickable(
            (By.XPATH,"//aside[@id='msg-overlay']/div[1]/header[1]/section[1]/button[1]")))
        time.sleep(2)
        element.click()
        print('Msg overlay hidden')

    except:
        print('msg overlay warning')







