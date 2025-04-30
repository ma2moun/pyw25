from flask import Flask, render_template
import sqlite3


app=Flask(__name__)

@app.route('/')
def index():
    conn=sqlite3.connect("showroom\\mycars.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO cars (brand, color, year) VALUES ('Toyota', 'pur', 2020)")
    cursor.execute("SELECT * FROM cars")
    cars=cursor.fetchall()
    conn.close()

    return render_template('index.html', cars=cars)

if __name__=='__main__':
    app.run(debug=True)

