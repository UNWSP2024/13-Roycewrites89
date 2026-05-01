#Royce Daniel, 5/1/2026, "Phonebook guts" Source: Gaddis, T. (2020). Starting Out with Python (5th ed.). Pearson Education (US). https://unwsp-bookshelf.vitalsource.com/books/9780136719199
import sqlite3

def main():
    conn = sqlite3.connect('phonebook.db')

    cur = conn.cursor()

    add_entries_table(cur)

    add_entries(cur)

    conn.commit()

    display_entries(cur)

    conn.close()


def add_entries_table(cur):

    cur.execute('DROP TABLE IF EXISTS Entries')


    cur.execute('''CREATE TABLE Entries (
                        Name TEXT PRIMARY KEY,
                        PhoneNumber TEXT
                   )''')

def add_entries(cur):
    phone_data = [
        ('Terence Fletcher', '555-1234'),
        ('Kirk Kirkland', '555-5678'),
        ('Jeffery Brown', '555-9012'),
        ('Tony Stark', '555-3456'),
        ('Ethan Winters', '555-7890'),
        ('Devin Stater', '555-1515'),
        ('Optimus Prime', '555-1984'),
        ('Tronald Dump', '555-8271'),
        ('Andrew Neiman', '555-3302'),
        ('Chris Redfeild', '555-4303'),
        ('Omni Man', '555-1111'),
        ('Jack Black', '555-6767'),
        ('Steve Jobs', '555-9091'),
        ('George Washington', '555-1776'),
        ('Mario Mario', '555-1984'),
        ('Tungtung Sahur', '555-6767'),
        ('Meghan Tron', '555-1984'),
        ('Keegan Key', '555-4444'),
        ('Jordan Peele', '555-6666'),
        ('Bruce Wayne', '555-4303'),
        ('Mata AM', '555-4312'),
        ('Scott Cawthon', '555-6916'),
        ('Walter White', '555-4421'),
        ('Anakin Skywalker', '555-1278'),
        ('Cassian Andor', '555-4771')
    ]

    for entry in phone_data:
        cur.execute('''INSERT INTO Entries (Name, PhoneNumber)
                       VALUES (?, ?)''', (entry[0], entry[1]))

def display_entries(cur):
    print('Contents of phonebook.db/Entries table:')
    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    for row in results:
        print(f'Name: {row[0]:20} Phone: {row[1]}')


if __name__ == '__main__':
    main()