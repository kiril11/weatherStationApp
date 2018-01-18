from flask import Flask, render_template, g
import sqlite3
import time

DATABASE = 'stationData.db'

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/')
def index():
    return render_template("projectOMT.html")


@app.route('/<cityname>')
def sofia(cityname):
    current_date = time.strftime("%d.%m.%y %H.%M.%S")
    g.db = connect_db()
    cur = g.db.execute("SELECT temp,date,hum FROM tabl WHERE city=(?) AND date<=(?)", (cityname,current_date,))
    result = [dict(city=cityname, temp=row[0], date=row[1], hum=row[2]) for row in cur.fetchall()]
    g.db.close()
    return render_template("projectOMT.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
