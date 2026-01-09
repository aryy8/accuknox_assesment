# for this problem I am using Open Library to fetch data and storing in sqlite database.
import requests
import sqlite3

def solve_problem_1():
    url = "https://openlibrary.org/search.json?q=python&limit=5"
    response = requests.get(url)
    data = response.json().get('docs', [])


    conn = sqlite3.connect('assessment.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books 
                      (title TEXT, author TEXT, year INTEGER)''')


    print("Books Saved")
    for item in data:
        title = item.get('title')

        author = item.get('author_name', ['Unknown'])[0]
        year = item.get('first_publish_year', 0)
        
        cursor.execute("INSERT INTO books VALUES (?, ?, ?)", (title, author, year))
        print(f"Stored: {title} by {author}")

    conn.commit()
    conn.close()

solve_problem_1()