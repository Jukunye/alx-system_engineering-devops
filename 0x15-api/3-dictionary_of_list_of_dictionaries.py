#!/usr/bin/python3
"""
Script that extend 'previous task 0' to export data in the JSON format.
"""
import json
import requests
from sys import argv


def get_employee_dict(user_id):
    url1 = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(url1)

    name = user_response.json().get("username")

    url2 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        user_id)

    todos = requests.get(url2).json()

    todos_list = [{"task": task["title"],
                   "completed": task["completed"],
                   "username": name}
                  for task in todos]

    return todos_list


if __name__ == "__main__":
    """not to be executed when imported"""
    data = {str(i): get_employee_dict(i) for i in range(1, 10)}

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)
