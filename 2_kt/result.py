import json
import csv


class Book:
    title: str
    author: str
    genre: str
    pages: int
    publisher: str


with open('books.csv', 'r') as file:
    books = []
    reader = csv.DictReader(file, fieldnames=['title', 'author', 'genre', 'pages', 'publisher'])
    header = next(reader)

for row in reader:
    current_book = Book()
    current_book.title = row['title']
    current_book.author = row['author']
    current_book.genre = row['genre']
    current_book.pages = row['pages']
    current_book.publisher = row['publisher']
    books.append(row)

with open('users.json', "r") as file:
    users = json.loads(file.read())

users_len = len(users)
books_len = len(books)
difference = books_len // users_len
small_users = []


def give_book(small_user, index):
    small_user['books'] = []
    for book_number in range(index, index + difference):
        small_user['books'].append(books[book_number])


index = 0
for user in users:
    small_user = dict()
    small_user['name'] = user['name']
    small_user['gender'] = user['gender']
    small_user['address'] = user['address']
    small_user['age'] = user['age']
    give_book(small_user, index)
    index += difference
    small_users.append(small_user)

for user_num in range(0, users_len):
    if index < books_len:
        small_users[user_num]['books'].append(books[index])
        index += 1

with open("result.json", "w") as file:
    s = json.dumps(small_users, indent=1)
    file.write(s)
