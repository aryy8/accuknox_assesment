# for this problem i am making a dummy csv file and then importing it into the same sqllite database as users.

import csv
import sqlite3

def solve_problem_3():

    with open('users.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'email'])
        writer.writerow(['aryan', 'aryan@google.com'])
        writer.writerow(['ayush', 'ayush@google.com'])
        writer.writerow(['raghav', 'raghav@google.com'])
        writer.writerow(['harhsi', 'harhsi@google.com'])


    conn = sqlite3.connect('assessment.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, email TEXT)')

    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                           (row['name'], row['email']))
    
    conn.commit()
    conn.close()
    print("\nCSV Data Imported")

solve_problem_3()