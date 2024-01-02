#!/usr/bin/python3
"""
Script that extend 'previous task 0' to export data in the CSV format.
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """not to be executed when imported"""
    url1 = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    user_response = requests.get(url1)

    name = user_response.json().get("username")

    url2 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])

    todos_response = requests.get(url2)
    todos = todos_response.json()

    data = [[(argv[1]), name, task["completed"], task["title"]]
            for task in todos]

    file_name = "{}.csv".format(argv[1])

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
