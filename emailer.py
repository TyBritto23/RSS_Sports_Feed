# Format and sends emails
import yagmail
from collections import defaultdict
from datetime import date

sportEmojis = ['⚾', '🏀']

# Run this once, so keyring saves email and password
# yagmail.register('CustomEmail@gmail.com', 'App Password')

# Create a custom body block so it looks nice, seperate it by sport
def sendEmail(newsList):
    organizedList = organizeBySport(newsList)
    body = createBody(organizedList)
    subject = "Daily Sports Digest"

    yag = yagmail.SMTP('CustomEmail@gmail.com')
    yag.send(
        to = 'yourEmail123@gmail.com',
        subject = subject,
        contents = body
    )


def organizeBySport(articles):
    grouped = defaultdict(list)

    for article in articles:
        sport = article[4]
        grouped[sport].append(article)

    return grouped


def createBody(list):
    todaysDate = date.today()
    formattedDate = todaysDate.strftime("%m-%d-%Y")
    html_parts = [f"<h1>Daily Sports Digest: {formattedDate}</h1>"]

    for sport, articles in list.items():
        if sport == 'mlb':
            html_parts.append(f"<h2 style='color:#1b4b6b;'>{sportEmojis[0]+ ' ' + sport.upper()+ ' ' + sportEmojis[0]}")
        elif sport == 'nba':
            html_parts.append(f"<h2 style='color:#1b4b6b;'>{sportEmojis[1]+ ' ' + sport.upper()+ ' ' + sportEmojis[1]}")
        else:
            html_parts.append(f"<h2 style='color:#1b4b6b;'>{sport.upper()}")

        for article in articles:
            title = article[1]
            url = article[2]
            summary = article[3]

            html_parts.append(f"""
                <p style='font-size:14px; line-height:1.5;'>
                    <strong>{title}</strong><br>
                    {summary}<br>
                    <a href="{url}">Read more</a>
                </p>
                <hr>
            """)

        body = "".join(html_parts)

    return body