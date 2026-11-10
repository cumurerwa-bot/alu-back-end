#!/usr/bin/python3
"""Gather employee TODO progress from an API."""

import json
import sys
from urllib.request import urlopen


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)

    with urlopen(user_url) as response:
        user = json.loads(response.read().decode("utf-8"))

    with urlopen(todos_url) as response:
        todos = json.loads(response.read().decode("utf-8"))

    completed_tasks = [
        task for task in todos if task.get("completed") is True
    ]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"),
            len(completed_tasks),
            len(todos)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
