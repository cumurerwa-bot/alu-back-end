#!/usr/bin/python3
"""Export employee TODO tasks to a JSON file."""

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

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    )
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    )

    with urlopen(user_url) as response:
        user = json.loads(response.read().decode("utf-8"))

    with urlopen(todos_url) as response:
        todos = json.loads(response.read().decode("utf-8"))

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    data = {"{}".format(user_id): tasks}

    filename = "{}.json".format(user_id)
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)
