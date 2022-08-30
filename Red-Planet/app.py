from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Missions_to_Mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/red_planet_db")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    redplanet = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", redplanet = redplanet)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # creating a redplanet database
    redplanet = mongo.db.redplanet

    # call the scrape function in our scrape_mars file. This will scrape and save to mongo.
    redplanet_data = Missions_to_Mars.scrape()

     # update our redplanet with the data that is being scraped.
    redplanet.update({}, redplanet_data, upsert=True)

  # return a message to our page so we know it was successful.   
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
