from flask import Flask, render_template, request, redirect, url_for
from uuid import uuid4
import sqlite3

app = Flask(__name__)

# Savieno datu bāzi ar python failu
db = sqlite3.connect("trenini.db", check_same_thread = False)
cur = db.cursor()

# Pie pardzētajiem URL "/......" izpilda funkcijas, piemēram, atver failus
@app.route("/")
def main():
    return render_template ("layout.html")
    


@app.route("/trenini")
def show_workouts():
    #No datubāzes aizsūta visus datus renderojot "trenini.html"
    res = cur.execute("SELECT * FROM trenini")
    trenini = res.fetchall()
    trenini.reverse()
    return render_template("trenini.html", data = trenini)


@app.route("/jauns_trenins", methods=["GET", "POST"])
def new_workout():
    #Pievieno datubāzei lietotāja ievadītos datus, ja metode ir "POST", jeb 
    # tiek nospiests "pievienot treniņu  
    if request.method == "POST":
        id = str(uuid4())
        datums = request.form["datums"]
        diena = request.form["diena"]
        musk_grupa = request.form["musk_grupa"]
        vingrinajums_1 = request.form["vingrinajums_1"]
        vingrinajums_2 = request.form["vingrinajums_2"]
        vingrinajums_3 = request.form["vingrinajums_3"]
        vingrinajums_4 = request.form["vingrinajums_4"]
        vingrinajums_5 = request.form["vingrinajums_5"]
        vingrinajums_6 = request.form["vingrinajums_6"]
        vingrinajums_7 = request.form["vingrinajums_7"]
        sql = '''INSERT INTO trenini
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cur.execute(sql, (id, datums, diena, musk_grupa, vingrinajums_1, vingrinajums_2, vingrinajums_3, vingrinajums_4, vingrinajums_5, vingrinajums_6, vingrinajums_7))
        db.commit()
        return redirect(url_for("main"))
    else:
        return render_template("jauns_trenins.html")
    
@app.route("/chest")
def show_chest():
    res = cur.execute("SELECT * FROM trenini")
    trenini = res.fetchall()
    return render_template("chest.html", data = trenini)

@app.route("/legs")
def show_legs():
    res = cur.execute("SELECT * FROM trenini")
    trenini = res.fetchall()
    return render_template("legs.html", data = trenini)

@app.route("/back")
def show_back():
    res = cur.execute("SELECT * FROM trenini")
    trenini = res.fetchall()
    trenini.reverse()
    return render_template("back.html", data = trenini)

@app.route("/tricep")
def show_tricep():
    res = cur.execute("SELECT * FROM trenini")
    trenini = res.fetchall()
    trenini.reverse()
    return render_template("tricep.html", data = trenini)

@app.route("/bicep")
def show_bicep():
    res = cur.execute("SELECT * FROM trenini")
    trenini = res.fetchall()
    trenini.reverse()
    return render_template("bicep.html", data = trenini)

@app.route("/shoulders")
def show_shoulder():
    res = cur.execute("SELECT * FROM trenini")
    trenini = res.fetchall()
    trenini.reverse()
    return render_template("shoulders.html", data = trenini)

@app.route("/nedelas_plans")
def show_plan():
    return render_template("nedelas_plans.html")

if __name__ == "__main__":
    app.run(debug=True)