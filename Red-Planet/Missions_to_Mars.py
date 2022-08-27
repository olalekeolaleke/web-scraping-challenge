#!/usr/bin/env python
# coding: utf-8

# In[16]:


# import Dependencies
import pandas as pd
from splinter import Browser
import os
from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request


# In[17]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)


# # NASA Mars News

# In[71]:


# Creating url path
url = 'https://redplanetscience.com/'


# In[72]:


# Sending HTTP request to the server
response = requests.get(url)
browser.visit(url)


# In[73]:


# Creating Beautiful soup object
html = browser.html
soup = bs(html, 'html.parser')
type(soup)


# In[74]:


# Printing formatted version of the soup
#print(soup.prettify())


# In[78]:


# Printing the entire article
article = soup.find("div", class_="list_text").text
print(article)


# In[76]:


# Printing the News Title

news_title = soup.find('div', class_= "content_title").text

print(f'The news title is "{news_title}"')


# In[77]:


# Printing the News Paragraph

news_p = soup.find("div", class_="article_teaser_body").text

print(f'The News paragraph ---- : {news_p}')


# # JPL Mars Space Images—Featured Image
# 

# In[26]:


# Setting featured image url
features_image_url = "https://spaceimages-mars.com/"


# In[27]:


# Sending http request to the server
response = requests.get(features_image_url)
browser.visit(features_image_url)


# In[28]:


# Creating Beautiful soup object
html = browser.html
soup = bs(html, 'html.parser')
type(soup)


# In[29]:


# Printing formatted version of the soup
#print(soup.prettify())


# In[40]:


# Printing featured image

featured_image_url = https://spaceimages-mars.com/image/featured/mars2.jpg"
print(featured_image_url)

img = soup.select_one("div.list_image")
img


# # Mars Facts

# In[31]:


# Setting up url
mars_fact_url = "https://galaxyfacts-mars.com/"


# In[32]:


# Visiting url and sending http requests to the server
browser.visit(mars_fact_url)
response = requests.get(mars_fact_url)


# In[33]:


# Creating Beautiful soup object
html = browser.html
soup = bs(html, 'html.parser')
type(soup)


# In[34]:


# Printing formatted version of the soup
#print(soup.prettify())


# In[35]:


# Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
mars_data = pd.read_html("https://space-facts.com/mars/")[0]

df = mars_data
df


# In[ ]:


# Using Pandas to convert the data to a HTML table string.
html = df.to_html()


# # Mars Hemispheres

# In[101]:


# Setting up url
astropedia_url = 'https://marshemispheres.com/'


# In[102]:


# Sending http request to the server
response = requests.get(astropedia_url)
browser.visit(astropedia_url)


# In[103]:


# Creating Beautiful soup object
html = browser.html
soup = bs(html, 'html.parser')
type(soup)


# In[104]:


# Printing formatted version of the soup
#print(soup.prettify())


# In[115]:


# Saving both the image url string for the full resolution hemisphere image,and the Hemisphere 
# title containing the hemisphere name

contents = soup.find_all("div", class_="item")

hemisphere_img_urls = []

for content in contents:
    hemisphere = {}

    title = content.find("h3").text
    link = content.find("a", class_="itemLink")["href"]
    hemisphere = url + link
    browser.visit(hemisphere)
    hemispherehtml = browser.html

    soup_2 = bs(hemispherehtml, "lxml")
    image = soup_2.find("img", class_="wide-image")["src"]
    img_url = url + image
    hemisphere = {}

    hemisphere_img_urls.append({"title":title,"img_url":img_url})

    


# Use a Python dictionary to store the data using the keys `img_url` and `title`
hemisphere_img_urls

