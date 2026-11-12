#!/usr/bin/python3
"""Export TODO tasks for all employees to a JSON file."""

import json
from urllib.request import urlopen


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    with urlopen(users_url) as response:
        users = json.loads(response.read().decode("utf-8"))

    with urlopen(todos_url) as response:
        todos = json.loads(response.read().decode("utf-8"))

    all_employees = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        all_employees[str(user_id)] = []

        for task in todos:
            if task.get("userId") == user_id:
                all_employees[str(user_id)].append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_employees, jsonfile)
