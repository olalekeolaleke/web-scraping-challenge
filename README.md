# web-scraping-challenge

This challenge involves building a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page

A Jupyter Notebook file called mission_to_mars.ipynb was used in scraping and analysing the tasks using BeautifulSoup, Pandas, and Requests/Splinter

The Mars News Site (https://redplanetscience.com/) was scraped and the latest News Title and Paragraph Text were collected and stored in variable called "news_title" and "news_p" respectively.

During the course of the assignment, https://spaceimages-mars.com was visited and Splinter was used to navigate the site and the image URL for the current Featured Mars Image was found, and the URL string was assigned to a variable called "featured_image_url"

The Mars Facts webpage (https://galaxyfacts-mars.com/) was also visited and Pandas was used to scrape the table containing facts about the planet including diameter, mass, etc. Pandas was then again used to convert the data to a HTML table string.

The astrogeology site was also visited to obtain high-resolution images for each hemisphere of Mars. Each of the links to the hemispheres was clicked in order to find the image URL to the full-resolution image

The image URL string for the full resolution hemisphere image and the hemisphere title containing the hemisphere name was saved. A Python dictionary was used to store the data using the keys "img_url" and "title".

The Jupyter notebook was converted into a Python script called "scrape_mars.py" by using a function called scrape. This function executes all your scraping code from above and return one Python dictionary containing all the scraped data

A route called "/scrape" that imports the "scrape_mars.py" script was created and the scrape function was then called

The return value was stored in Mongo as a Python dictionary and a root route / was created that queries the Mongo database and pass the Mars data into an HTML template for displaying the data

A template HTML file called index.html was created, which takes the Mars data dictionary and display all the data in the appropriate HTML elements.

Lastly, MongoDB with Flask templating was used to create a new HTML page that displays all the information that was scraped from the above URLs
