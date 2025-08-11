# Lists of RSS feed URLs and logic to fetch them
# Will later add this to a database
import feedparser
from fParser import parse_feed
from database import insertIntoDB, getSizeOfDB

RSS_FEEDS = [
   {"URL": "https://www.espn.com/espn/rss/news",     "sport": "top"},
   {"URL": "https://www.espn.com/espn/rss/mlb/news", "sport": "mlb"}, 
   {"URL": "https://www.espn.com/espn/rss/nba/news", "sport": "nba"} 
]

# Function to fetch and parse the RSS feed for a given sport
# Add custom URL RSS feed option later
def fetch_feed(sport):
    url = sport['URL']
    parsedData = feedparser.parse(url)
    if parsedData.bozo:
        raise ValueError(f"Failed to parse RSS feed for {sport['sport']}: {parsedData.bozo_exception}")
    return parsedData


def getFeedData():
    feed_data = []

    for i in RSS_FEEDS:
        feed_data += parse_feed(fetch_feed(i), i['sport'])  
    
    return feed_data
