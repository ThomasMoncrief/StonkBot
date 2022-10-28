#Apply for a Reddit API key at: https://www.reddit.com/prefs/apps (this will only require a 'script' application)
#For redirectURI, use local host: http://localhost:8080/
#fill in "client_id" and "client_secret" with your "Personal Use Script" and "Secret" that Reddit gives you.
#Adjust the indexing in line 20 to get more than 100 comments.

import praw, string

def reddit_connect():
    reddit = praw.Reddit(
        client_id = "######",
        client_secret = "######",
        user_agent = "my user agent",
        username = "",
        password = "",
    )
    print(reddit.read_only)
    return reddit

def print_from_subreddit(reddit_connect, subreddit):
    WSB_comments = []
    for post in reddit_connect.subreddit(subreddit).hot(limit=1):
        for x in post.comments[0:100]:
            WSB_comments.append(x.body)

    WSB_comments = ' '.join(WSB_comments)
    WSB_comments = WSB_comments.lower()
    WSB_comments = WSB_comments.translate(str.maketrans('', '', string.punctuation))
    return WSB_comments

print(print_from_subreddit(reddit_connect(), "wallstreetbets"))
