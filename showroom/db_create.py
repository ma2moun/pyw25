import sqlite3

# Delete after using

conn=sqlite3.connect("mycars.db")
cursor=conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS cars (
                   id INTEGER PRIMARY KEY,
                   brand TEXT,
                   color TEXT,
                   year INTEGER
               )
               ''')

cursor.execute("INSERT INTO cars (brand, color, year) VALUES ('Toyota', 'Red', 2009)")
cursor.execute("INSERT INTO cars (brand, color, year) VALUES ('BMW', 'White', 2020)")
cursor.execute("INSERT INTO cars (brand, color, year) VALUES ('Nissan', 'Black', 2000)")


conn.commit()
conn.close()

print(f"Table was created successfully!")
