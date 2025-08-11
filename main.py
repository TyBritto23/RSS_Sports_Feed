# Will combine all the components (fetch -> parse  -> email-> log into DB)

import database
import feeds
import emailer


# Get feed data and parse it
parsedFeeds = feeds.getFeedData()


# Add into the database
database.insertIntoDB(parsedFeeds)

unsentArticles = database.getUnsentArticles()


emailer.sendEmail(unsentArticles)
