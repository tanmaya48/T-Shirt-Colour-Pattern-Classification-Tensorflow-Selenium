from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import requests
import shutil
import os
import sys



name = 'red checkers t shirt'  ## search for anything you want



shirts = [ ['red','plain'],['red','check'],['red','striped'],
['blue','plain'],['blue','check'],['blue','striped'],
['green','plain'],['green','check'],['green','striped'] ]


opts = Options()

opts.headless=True


browser = Firefox(options=opts)  ## should include webdriver as arguement if webdriver not in /usr/local/bin/

i=1000


file = open('shirts.csv','w')


for color , pattern in shirts:


    name = color + ' ' + pattern + ' shirt'  

    browser.get('https://duckduckgo.com')
    search_form = browser.find_element_by_id('search_form_input_homepage') ## search box
    search_form.send_keys(name)
    search_form.submit()
    browser.implicitly_wait(1)   ## wait for page to load
    browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/ul[1]/li[2]/a').click()   ## images button
    browser.implicitly_wait(3)  ## wait for page to load
    images = browser.find_elements_by_class_name('tile--img__img') ## class of image display
    print(len(images))

    for image in images:

        file.write(str(i) + ',' + color + ',' + pattern + '\n')

        image_link = image.get_attribute('data-src')[19:]   ## data source  [19:] since source starts with //external-content.
        image_file = requests.get('https://'+image_link,stream=True)  ## get file

        if image_file.status_code == 200:   ## if downloaded correctly
            image_file.raw.decode_content = True
        
        ## Open a local file with wb ( write binary ) permission.
            with open(str(i),'wb') as f:             
                shutil.copyfileobj(image_file.raw, f)
            i+=1



file.close()

browser.close()
