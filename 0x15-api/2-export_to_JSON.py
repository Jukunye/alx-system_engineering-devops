#!/usr/bin/python3
"""
Script that extend 'previous task 0' to export data in the CSV format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """not to be executed when imported"""
    url1 = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    user_response = requests.get(url1)

    name = user_response.json().get("username")

    url2 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])

    todos = requests.get(url2).json()

    todos_list = [{"task": task["title"],
                   "completed": task["completed"],
                   "username": name}
                  for task in todos]

    todos_dict = {argv[1]: todos_list}

    with open(argv[1] + ".json", "w") as json_file:
        json.dump(todos_dict, json_file)
