# Code snippet to extract data
from selenium import webdriver
import pandas as pd
import time
import os.path

# Path of the folder to store the txt files 
save_path = 'files' 
data_extracted =[]
# Read the links from Input excel file
df = pd.read_excel('Input.xlsx',index_col=False)
df= df.drop(['URL_ID'], axis = 1)
j=0
# loop the links to extract the data from website
for i in df['URL']:
    j+=1
    browser = webdriver.Chrome("chromedriver.exe")
    browser.get(i)
    time.sleep(5)
    title = browser.find_element_by_xpath("/html/body/div[6]/article/div[1]/div[1]/div[2]/div[2]/header/h1")
    try:
        data = browser.find_element_by_class_name("td-post-content")
    except:
        data = browser.find_element_by_class_name("wp-block-preformatted")
    data=data.text
    article_content = data.strip()
    data_extracted.append(title.text)
    data_extracted.append(article_content)
    completeName = os.path.join(save_path, str(j)+".txt")  
    with open( completeName, 'w', encoding='utf-8') as f:
        for term in data_extracted:
            f.write(term)
    browser.quit()
