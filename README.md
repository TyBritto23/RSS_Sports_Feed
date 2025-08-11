# Sports Digest Emailer

This project fetches the latest sports articles, organizes them by sport, and sends a clean, formatted daily email digest.

I made this to stay update with sports news without having to rely on social media.

---

# Features
- **Automated News Fetching** – Scrapes and stores sports articles in an SQLite database.
- **Categorized Email Digest** – Groups articles by sport with bold section headers.
- **Duplicate Protection** – Uses `INSERT OR IGNORE` to avoid adding duplicates.
- **Status Tracking** – Marks articles as `sent` after emailing to prevent repeats.
- **Secure Email Sending** – Uses `yagmail` + `keyring` to avoid storing passwords in code.

---

# How To Use
## 1. Setup
- **Clone the Repository**: `git clone https://github.com/TyBritto23/RSS_Sports_Feed.git`
- **Install UV for python**: This is optional, but helpful. I used [uv](https://docs.astral.sh/uv/) and its virtual environment to deal with the project dependencies as it makes it pretty easy
- **Set up an Email**: Create a custom email with an app password, this is what will send you the email, and add it into the emailer.py file, `yagmail.register('CustomEmail@gmail.com', 'App Password')`
- **Add your own email**: Within the emailer.py file you need to add the email you would like the sports news to be sent to.
- **Run**: If your using [uv](https://docs.astral.sh/uv/) and its virtual environment you can test run the project by pasting `uv run main.py` into your terminal

## 2. Automating the Email
- If you're using MacOS or Linux I would suggest using crontab (This is what I'm using) or use Task Scheduler on Windows.
- If you are using crontab here's how you can set it up:
```
#this will open a vim text editor
crontab -e

# Paste this in the text editor and save, make sure you update the directories so they're correct
0 8 * * * /home/yourname/projects/sports_digest/venv/bin/python /home/yourname/projects/sports_digest/main.py >> /home/yourname/projects/sports_digest/digest.log 2>&1

```
- You can also use Cloud services such as GitHub Actions or [PythonAnywhere](https://www.pythonanywhere.com/)
- 

---

# Contributions and Future Features
- Anyone is welcome to contribute towards this project
- I don't plan on adding any new features at this point, as it does all I need it to, but I may make it more user friendly in the future






