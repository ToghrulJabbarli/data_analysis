#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import bs4
import pandas as pd


# In[6]:


def scrape_url(url_string,max):
    titles=[]
    prices=[]
    ratings=[]
    shipment=[]
    for page in range(max):
        url = url_string + str(page)
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        driver.get(url)
        content = driver.page_source
        soup = bs4.BeautifulSoup(content)
    
        for k in soup.find_all('div', attrs={'class':'a-section a-spacing-base'}):
            title=k.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
            price=k.find('span', attrs={'class':'a-offscreen'})
            rating=k.find('span', attrs={'class':'a-icon-alt'})
            ship=k.find('span', attrs={'class':'a-size-small a-color-base'})
            if title is None:
                titles.append("")
            else:
                titles.append(title.text)
            if price is None:
                prices.append("")
            else:
                prices.append(price.text)
            if rating is None:
                ratings.append("")
            else:
                ratings.append(rating.text)
            if ship is None:
                shipment.append("")
            else:
                shipment.append(ship.text)
            
            
    return list(zip(titles,prices,ratings,shipment))
        
if __name__ == "__main__":
    url_string="https://www.amazon.com/s?bbn=16225009011&rh=n%3A2811119011&page="
    datas=scrape_url(url_string,1)
    df = pd.DataFrame(datas,columns=('Title','Price','Rating','Shipment Detail'))

