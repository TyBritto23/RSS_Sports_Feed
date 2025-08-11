# SQlite3 setup and helper functions
# Add .db file to the .gitignore file
import sqlite3

with sqlite3.connect("rss_digest.db") as connection:
    cursor = connection.cursor()

   # Create table if it doesn't exist
    # cursor.execute("DROP TABLE IF EXISTS articles") # remove before production
    cursor.execute("""CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        url TEXT UNIQUE,
        summary TEXT,
        sport TEXT,
        published TEXT,
        sent INTEGER
    )""") 

    # Add check to see if article is already in db
    def insertIntoDB(parsedItems):
        for i in range(len(parsedItems)):
            cursor.execute("""
            INSERT OR IGNORE INTO articles (
            title, url, summary, sport, published, sent
        ) VALUES (?, ?, ?, ?, ?, ?)""", (
            parsedItems[i]['title'],
            parsedItems[i]['url'],
            parsedItems[i]['summary'],
            parsedItems[i]['sport'],
            parsedItems[i]['published'],
            0
        ))


        connection.commit()

            
    def getSizeOfDB():
        cursor.execute("SELECT * FROM articles WHERE sent=0")
        print(len(cursor.fetchall()))

    def getUnsentArticles():
        unsent = cursor.execute("SELECT * FROM articles WHERE sent = 0")
        # markArticlesAsSent(unsent)
        return unsent.fetchall()
    
    def getSentArticles():
        unsent = cursor.execute("SELECT * FROM articles WHERE sent = 1")
        return unsent.fetchall()

    def markArticlesAsSent(sent):
        ids = [str(article[0]) for article in sent]
        if ids:
            cursor.execute(f"UPDATE articles SET sent = 1 WHERE id IN ({','.join(ids)})")

        connection.commit()

    def markArticlesAsSent(sent):
        ids = [str(article[0]) for article in sent]
        if ids:
            cursor.execute(f"UPDATE articles SET sent = 0 WHERE id IN ({','.join(ids)})")

        connection.commit()



    def check():
        cursor.execute("SELECT * FROM articles WHERE sent=0")
        rows = cursor.fetchall()
        print("rows count:", len(rows))
        for i, r in enumerate(rows[:10]):   # print up to first 10 rows
            print(i, type(r), repr(r))
            try:
                print("  len:", len(r))
            except Exception as e:
                print("  len error:", e)
