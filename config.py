from collections import namedtuple

Config = namedtuple('Config', ["subreddits", "bot_name", "keywords", "notify_command", "timeout"])

bot_config = Config(
            subreddits=['slavelabour', 'forhire', 'sellmyskill', 'freelance_forhire', 'Jobs4Scrapers', 'Jobs4Bitcoins', 'DeveloperJobs', 'jobbit'],
            bot_name="Python notification bot",
            keywords=['hiring', 'task'],
            notify_command="dunstify -t 0".split(),
            timeout=300,
)

