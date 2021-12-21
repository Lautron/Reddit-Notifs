from collections import namedtuple

Config = namedtuple('Config', ["subreddits", "bot_name", "keywords", "notify_command", "timeout"])

bot_config = Config(
            subreddits=[
                'slavelabour', 'forhire', 'sellmyskill',
                'freelance_forhire', 'Jobs4Scrapers', 'Jobs4Bitcoins',
                'DeveloperJobs', 'jobbit'
            ], # Subreddits to scrape
            bot_name="Name of the bot", # User agent
            keywords=['hiring', 'task'], # keywords that have to be in post
            notify_command="notify-send -t 0", # Command to send the notification 
            timeout=300, #seconds
)

#"dunstify -t 0",
