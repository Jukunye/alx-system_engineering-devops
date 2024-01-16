#!/usr/bin/python3
"""
Contains a function that queries the Reddit API and
returns the number of subscribers (not active users, total subscribers)
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Setting up a custom User-Agent to avoid too many Request errors
    headers = {'User-Agent': 'Google Chrome Version 120.0.6099.217'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data").get("subscribers")
        return data
    return 0
