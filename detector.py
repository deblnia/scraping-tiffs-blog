import smtplib
from email.mime.text import MIMEText

import feedparser

# Blog URL
RSS_FEED_URL = "https://final545.blogspot.com/"
# SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
FROM_EMAIL = ""
PASSWORD = ""


def get_latest_post_url():
    """Get the URL of the latest post from the RSS feed"""
    feed = feedparser.parse(RSS_FEED_URL)
    if not feed.entries:
        print("Error: No entries found in the RSS feed")
        return None
    latest_post = feed.entries[0]
    return latest_post.link


def send_email(subject, body):
    """Send an email notification using SMTP"""
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = FROM_EMAIL
    msg["To"] = FROM_EMAIL  # Send to yourself for now
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(FROM_EMAIL, PASSWORD)
    server.sendmail(FROM_EMAIL, FROM_EMAIL, msg.as_string())
    server.quit()


def main():
    latest_post_url = get_latest_post_url()
    if latest_post_url:
        send_email(
            "New Post on final545.blogspot.com!",
            f"Check out the latest post: {latest_post_url}",
        )


if __name__ == "__main__":
    main()
