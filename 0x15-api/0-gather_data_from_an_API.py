#!/usr/bin/python3
"""
Script that using a REST API, for a given employee ID,
returns information about his/her todo list progress.
"""
from sys import argv
import requests


if __name__ == "__main__":
    """not to be executed when imported"""
    url1 = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    user_response = requests.get(url1)

    name = user_response.json().get("name")

    url2 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])
    
    todos_response = requests.get(url2)
    todos = todos_response.json()
    todos_total = len(todos)
    completed = sum(task["completed"] for task in todos)

    employee = "Employee {} is done with tasks({}/{})".format(
        name, completed, todos_total
    )
    print(employee)

    for task in todos:
        if task["completed"]:
            print("\t {}".format(task["title"]))
