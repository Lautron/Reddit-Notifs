from collections import namedtuple

Config = namedtuple(
    "Config",
    [
        "subreddits",
        "bot_name",
        "keywords",
        "notify_command",
        "timeout",
        "max_time_since_creation",
    ],
)

bot_config = Config(
    subreddits=[
        "slavelabour",
        "forhire",
        "sellmyskill",
        "freelance_forhire",
        "Jobs4Scrapers",
        "Jobs4Bitcoins",
        "DeveloperJobs",
        "jobbit",
    ],  # Subreddits to scrape
    bot_name="Custom Reddit Notification Bot",  # User agent
    keywords=[
        "[hiring]",
        "[task]",
    ],  # keywords that have to be in post, write without spaces
    notify_command="dunstify -t 0",  # Command to send the notification
    timeout=600,  # seconds
    max_time_since_creation=600,  # Max time since creation in minutes
)

# "dunstify -t 0",
