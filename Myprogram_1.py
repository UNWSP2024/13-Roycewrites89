#Royce Daniel, 5/1/2026. "cities database"
import sqlite3
conn = sqlite3.connect('cities.db')
def main():
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()


    def display_entries(cur):
        cur.execute("SELECT * FROM cities")
        results = cur.fetchall()
        if results:
            print("\n--- CITY ENTRIES ---")
            for row in results:
                print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')
        else:
            print("No entries found.")


    display_entries(cur)
    conn.commit()
    conn.close()

 # Execute the main function.
if __name__ == '__main__':
        main()

