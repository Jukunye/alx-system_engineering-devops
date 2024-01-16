#!/usr/bin/python3
"""
Contains the function def top_ten(subreddit)
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Setting up a custom User-Agent to avoid too many Request errors
    headers = {'User-Agent': 'Google Chrome Version 120.0.6099.217'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data_list = response.json().get("data").get("children")
        for i in range(0, 10):
            print(data_list[i].get("data").get("title"))
    else:
        print(None)
