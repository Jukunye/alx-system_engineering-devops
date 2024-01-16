#!/usr/bin/python3
"""
Contains the function def recurse(subreddit, hot_list=[], params=None)
"""
import requests


def recurse(subreddit, hot_list=[], params=None):
    """
    recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Setting up a custom User-Agent to avoid too many Request errors
    headers = {'User-Agent': 'Google Chrome Version 120.0.6099.217'}

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        data_list = data.get("children")
        for hot in data_list:
            hot_list.append(hot.get("data").get("title"))

        after = data.get("after")

        if after:
            params = {"after": after, "limit": 100}
            recurse(subreddit, hot_list=hot_list, params=params)
        return hot_list
    return None
