# import Dependencies
import pandas as pd
from splinter import Browser
import os
from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import urllib3


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

redplanet = {}

# Creating url path
url = 'https://redplanetscience.com/'

# Sending HTTP request to the server
response = requests.get(url)
browser.visit(url)


# Creating Beautiful soup object
html = browser.html
soup = bs(html, 'html.parser')

# Printing the entire article
article = soup.find("div", class_="list_text").text

# Printing the News Title
news_title = article.find('div', class_= "content_title").text
redplanet["news_title"] = news_title

# Printing the News Paragraph
news_p = article.find("div", class_="article_teaser_body").text
redplanet["news_p"] = news_p


# JPL Mars Space Images—Featured Image
featured_image_url = "https://spaceimages-mars.com/image/featured/mars2.jpg"
redplanet["featured_image_url"] = featured_image_url

# Setting featured image url
img_url = "https://spaceimages-mars.com"

# Setting up url
mars_fact_url = "https://galaxyfacts-mars.com/"

# Visiting url and sending http requests to the server
browser.visit(mars_fact_url)
response = requests.get(mars_fact_url)

# Creating Beautiful soup object
html = browser.html
soup = bs(html, 'html.parser')

# Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
mars_data = pd.read_html("https://space-facts.com/mars/")[1]

df = mars_data
df.set_index('Mars - Earth Comparison', inplace=True)
df
# Using Pandas to convert the data to a HTML table string.
html_table = df.to_html()


# Setting up url
base_url = 'https://marshemispheres.com/'

# Sending http request to the server
response = requests.get(base_url)
browser.visit(base_url)


# Creating Beautiful soup object
html = browser.html
soup = bs(html, 'html.parser')


# Saving both the image url string for the full resolution hemisphere image,and the Hemisphere 
# title containing the hemisphere name

hemisphere_img_urls = []

contents = soup.find_all("div", class_="item")

for content in contents:
    hemisphere = {}

    title = content.find("h3").text
    link = content.find("a", class_="itemLink")["href"]
    hemisphere = base_url + link
    browser.visit(hemisphere)
    hemispherehtml = browser.html

    soup2 = bs(hemispherehtml, 'html.parser')
    image = soup2.find("img", class_= "wide-image")["src"]
    img_url = base_url + image
    hemisphere = {}

    hemisphere_img_urls.append({"title":title,"img_url":img_url})


# Use a Python dictionary to store the data using the keys `img_url` and `title`
hemisphere_img_urls
