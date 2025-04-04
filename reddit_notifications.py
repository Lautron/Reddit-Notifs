import requests
import json
import time
import threading
import subprocess
from config import bot_config
import os


class Subreddit:
    def __init__(self, name):
        self.name = name
        self.seen_posts = set()
        self._get_existing_posts()

    def _get_subreddit_data(self):
        json_res = requests.get(
            f"https://www.reddit.com/r/{self.name}/new.json",
            headers={"User-agent": bot_config.bot_name},
        )
        json_res.raise_for_status()

        if not json_res.ok:
            print("Server responded:", json_res.status_code)
            return []

        sub_data = json.loads(json_res.content)["data"]["children"]
        return sub_data

    def _get_existing_posts(self):
        existing_posts = {
            post.title
            for post in self.get_posts()
            if post.mins_since_creation() > bot_config.max_time_since_creation
        }

        self.seen_posts.update(existing_posts)

    def get_posts(self):
        sub_data = self._get_subreddit_data()
        return [Post(post_data["data"]) for post_data in sub_data]


class Post:
    def __init__(self, post_data):
        self.title = post_data["title"]
        self.created_on = post_data["created_utc"]
        self.link = "www.reddit.com" + post_data["permalink"]

    def __repr__(self):
        return f"({self.title}\n{self.time_since_creation()}\n{self.link})\n"

    def mins_since_creation(self):
        time_since = time.time() - int(self.created_on)
        res = time_since // 60
        return res

    def time_since_creation(self):
        minutes_since = self.mins_since_creation()
        hours_since = minutes_since // 60
        if minutes_since < 60:
            return f"{minutes_since} minutes"
        else:
            return f"{hours_since} hours"

    def has_keyword(self):
        formatted_title = self.title.lower().replace(" ", "")
        for keyword in bot_config.keywords:
            if keyword in formatted_title:
                # print(f"{lowercase_title}:  {keyword}")
                return True

        return False

    def notify(self, sub_name):
        message = f"New post on r/{sub_name}:\n{self.title}\nPosted {
            self.time_since_creation()} ago\n{self.link}\n"
        print(message)
        notif_data = [self.title, self.link]
        subprocess.Popen(bot_config.notify_command.split() + notif_data)


def search_sub(subreddit_name):
    sub = Subreddit(subreddit_name)
    def is_valid(
        post): return post.title not in sub.seen_posts and post.has_keyword()
    print(f"Started watching for new posts on r/{sub.name}...")
    while True:
        print(f"Searching r/{sub.name}...\n")
        if os.environ.get("STOP_REDDIT_NOTIFS"):
            print(f"Stopped watching for new posts on r/{sub.name}...")
            return
        for post in sub.get_posts():
            if is_valid(post):
                sub.seen_posts.add(post.title)
                post.notify(sub.name)
        time.sleep(bot_config.timeout)


def main():
    for sub in bot_config.subreddits:
        x = threading.Thread(target=search_sub, args=(sub,))
        x.start()
        time.sleep(1)


if __name__ == "__main__":
    main()
