#Royce Daniel, 5/1/2026, "Phonebook"
import sqlite3

def main():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()


    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Add Entry")
        print("2. Update Entry")
        print("3. Delete Entry")
        print("4. Display All Entries")
        print("5. End Program")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_entry(cur, conn)
        elif choice == '2':
            update_entry(cur, conn)
        elif choice == '3':
            delete_entry(cur, conn)
        elif choice == '4':
            display_entries(cur)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

    conn.close()



# CREATE
def add_entry(cur, conn):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    try:
        cur.execute("INSERT INTO Entries (Name, PhoneNumber) VALUES (?, ?)", (name, phone))
        conn.commit()
        print("Entry added.")
    except sqlite3.IntegrityError:
        print("That name already exists.")



# UPDATE
def update_entry(cur, conn):
    name = input("Enter name to update: ")
    cur.execute("SELECT * FROM Entries WHERE Name = ?", (name,))

    if cur.fetchone():
        new_phone = input("Enter new phone number: ")
        cur.execute("UPDATE Entries SET PhoneNumber = ? WHERE Name = ?", (new_phone, name))
        conn.commit()
        print("Entry updated.")
    else:
        print("Entry not found.")


# DELETE
def delete_entry(cur, conn):
    name = input("Enter name to delete: ")
    cur.execute("SELECT * FROM Entries WHERE Name = ?", (name,))

    if cur.fetchone():
        cur.execute("DELETE FROM Entries WHERE Name = ?", (name,))
        conn.commit()
        print("Entry deleted.")
    else:
        print("Entry not found.")


# DISPLAY ALL
def display_entries(cur):
    cur.execute("SELECT * FROM Entries")
    results = cur.fetchall()

    if results:
        print("\n--- PHONEBOOK ENTRIES ---")
        for row in results:
            print(f"Name: {row[0]:20} Phone: {row[1]}")
    else:
        print("No entries found.")


if __name__ == '__main__':
    main()