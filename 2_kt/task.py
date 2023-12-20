import json
import csv
from csv import DictReader
import os.path
import math

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


JSON_FILE_PATH = get_path(filename="users.json")
CSV_FILE_PATH = get_path(filename="books.csv")


with open(CSV_FILE_PATH, newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    books_list = []
    for row in reader:
        books_list.append(dict(zip(header, row)))


with open(JSON_FILE_PATH, "r") as f:
    users_list = json.loads(f.read())

users_len = len(users_list)
books_len = len(books_list)


difference = math.floor(books_len / users_len)


user = 0
for i in range(0, books_len + difference - 1, difference):
    if user == users_len:
        break
    users_list[user]["BOOKS"] = []
    for book in range(i, i + difference):
        users_list[user]["BOOKS"].append(books_list[book])
    user += 1

for i in range(0, users_len):
    if user * difference + i < books_len:
        users_list[i]["BOOKS"].append(books_list[user * difference + i])


with open("result.json", "w") as f:
    s = json.dumps(users_list, indent=4)
    f.write(s)