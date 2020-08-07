#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 14:04:20 2020

@author: yuanzhuang
"""
import time
from selenium.common.exceptions import NoSuchElementException

# one-time only
def login(driver):
    Email = 'johnzanzan@gmail.com'
    Password = 'Acsk070743'
    url = 'https://www.linkedin.com/home'
    

    driver.get(url)
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
    element = driver.find_element_by_xpath("//aside[@id='msg-overlay']/div[1]/header[1]/section[1]/button[1]")
    element.click()
    time.sleep(2)
