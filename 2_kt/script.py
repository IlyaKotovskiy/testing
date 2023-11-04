import csv
import json

with open('users.json', 'r') as users_file:
    users_data = json.load(users_file)

with open('books.csv', 'r', newline='') as books_file:
    books_data = list(csv.DictReader(books_file))

num_users = len(users_data)
num_books = len(books_data)
books_per_user = num_books // num_users
remaining_books = num_books % num_users

result = []

for i, user in enumerate(users_data):
    books_for_user = books_per_user + (1 if i < remaining_books else 0)
    user_books = []

    for j in range(books_for_user):
        book_data = books_data.pop(0)
        book = {
            "title": book_data["Title"],
            "author": book_data["Author"],
            "genre": book_data["Genre"],
            "pages": int(book_data["Pages"])
        }
        user_books.append(book)

    user_info = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": user_books
    }
    result.append(user_info)

with open('result.json', 'w') as result_file:
    json.dump(result, result_file, indent=4)

print("Создан файл result.json")