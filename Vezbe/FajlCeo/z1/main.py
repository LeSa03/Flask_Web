import flask
from flask import Flask

app = Flask(__name__, static_url_path="/")


studenti = [
    {"brojIndeksa": "1234/123456", "ime": "Marko", "Prezime": "Petrovic", "ProsecnaOcena": 7.2},
    {"brojIndeksa": "1235/123457", "ime": "Stef", "Prezime": "Cuka", "ProsecnaOcena": 6.2},
    {"brojIndeksa": "1236/123458", "ime": "Borko", "Prezime": "Dlake", "ProsecnaOcena": 8.2},
    {"brojIndeksa": "1237/123459", "ime": "Mile", "Prezime": "Dzuka", "ProsecnaOcena": 9.2},
]

@app.route("/")
@app.route("/home")
@app.route("/home.html")
@app.route("/index")
@app.route("/index.html")
def home():
    return flask.render_template("tabela.tpl.html", studenti=studenti)

@app.route("/formaDodavanje")
def forma_za_dodavanje_studenta():
    return flask.render_template("student_forma.tpl.html")


@app.route("/dodajStudenta", methods=["POST"])
def dodavanje_studenta():
    student = dict(flask.request.form)
    studenti.append(student)
    return flask.redirect("/")


@app.route("/ukloni")
def uklanjanje_studenta():
    broj_indeksa = flask.request.args.get("student")
    for i, student in enumerate(studenti):
        if broj_indeksa == student["brojIndeksa"]:
            studenti.pop(i)
            return flask.redirect("/")
    return flask.redirect("/", 404)


@app.route("/izmeni", methods=["GET"])
def forma_Za_Izmenu():
    broj_indeksa = flask.request.args.get("student")
    student_za_izmenu = None
    for student in studenti:
        if student["brojIndeksa"] == broj_indeksa:
            student_za_izmenu = student

    if student_za_izmenu is None:
        return "Nije pronadjen!", 404
    
    return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="script.js" defer></script>
</head>
<body>
    <form onsubmit="validacija()" action="/izmeni?student={broj_indeksa}" method="post">

        <div>
            <label for="broj-indeksa">Broj Ideksa</label>
            <input id="broj-indeksa" type="text" name="brojIndeksa" value="{student_za_izmenu['brojIndeksa']}" required>
        </div>

        <div>
            <label>ime <input type="text" name="ime" value="{student_za_izmenu['ime']}" required></label>
        </div>

        <div>
            <label>Prezime <input type="text" name="prezime" value="{student_za_izmenu['Prezime']}" required></label>
        </div>

        <div>
            <label>Prosecna ocena <input type="number" min="5" max="10" step="0.01" name="prosecnaOcena" value="{student_za_izmenu['ProsecnaOcena']}" required></label>
        </div>
       
        <div>
            <button type="submit">Dodaj</button>
        </div>

    </form>

</body>
</html>
'''

@app.route("/izmeni", methods=["POST"])
def izmeni_studenta():
    broj_indeksa = flask.request.args.get("student")
    for i, student in enumerate(studenti):
        if student["brojIndeksa"] == broj_indeksa:
            studenti[i] = dict(flask.request.form)
            return flask.redirect("/")
        
    return "Nije pronadjen student za izmenu!", 404


if __name__ == "__main__":
    app.run()