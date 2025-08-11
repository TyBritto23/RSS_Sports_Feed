# Will parse RSS feeds and extract relevant information
import feedparser

# Extracts relevant data from all entries and returns it as a array dictionary
def parse_feed(feed, sport):
    if not feed or not feed.entries:
        raise ValueError("No entries found in the feed")
    
    entries = feed.entries # Gets the first entry in the feed
    count = len(feed.items())
    parsed_entries = [{} for _ in range(count)]
    # for entry in entries:
    for i in range(count):
        entry = feed.entries[i]
        parsed_entries[i] = {
            "title": entry.title,
            "url": entry.link,
            "published": entry.published,
            "summary": entry.summary,
            "sport": sport,
        }


    return parsed_entries