import flask
from flask import Flask

app = Flask(__name__, static_url_path="/")


studijski_programi = [
    {"sifra": "SII", "naziv" : "Soft. inz."},
    {"sifra" : "IT", "naziv" : "Inf. teh."}
]

studenti = [
    {"brojIndeksa": "1234/123456", "ime": "Marko", "Prezime": "Petrovic", "ProsecnaOcena": 7.2, "smer": {"sifra": "SII", "naziv" : "Soft. inz."}, "aktivan" : True},
    {"brojIndeksa": "1235/123457", "ime": "Stef", "Prezime": "Cuka", "ProsecnaOcena": 6.2, "smer": {"sifra": "SII", "naziv" : "Soft. inz."}, "aktivan" : True},
    {"brojIndeksa": "1236/123458", "ime": "Borko", "Prezime": "Dlake", "ProsecnaOcena": 8.2, "smer": {"sifra": "SII", "naziv" : "Soft. inz."}, "aktivan" : True},
    {"brojIndeksa": "1237/123459", "ime": "Mile", "Prezime": "Dzuka", "ProsecnaOcena": 9.2, "smer": {"sifra": "SII", "naziv" : "Soft. inz."}, "aktivan" : True},
]

@app.route("/")
@app.route("/home")
@app.route("/home.html")
@app.route("/index")
@app.route("/index.html")
def home():
    aktivni_studenti = list(filter(lambda s: s["aktivan"], studenti))
    return flask.render_template("tabela.tpl.html", studenti=aktivni_studenti)

@app.route("/formaDodavanje")
def forma_za_dodavanje_studenta():
    return flask.render_template("student_forma.tpl.html", student=None, studijski_programi=studijski_programi)


@app.route("/dodajStudenta", methods=["POST"])
def dodavanje_studenta():
    student = dict(flask.request.form)
    student["aktivan"] = True

    smer = list(filter(lambda s: s["sifra"] == student["smer"], studijski_programi))
    if len(smer) > 0:
        student["smer"] = smer[0]
    else:
        student["smer"] = None

    studenti.append(student)
    return flask.redirect("/")


@app.route("/ukloni")
def uklanjanje_studenta():
    broj_indeksa = flask.request.args.get("student")
    for i, student in enumerate(studenti):
        if broj_indeksa == student["brojIndeksa"]:
            # studenti.pop(i)
            studenti[i]["aktivan"] = False
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
    
    return flask.render_template("student_forma.tpl.html", student=student_za_izmenu, studijski_programi=studijski_programi)


@app.route("/izmeni", methods=["POST"])
def izmeni_studenta():
    broj_indeksa = flask.request.args.get("student")
    for i, student in enumerate(studenti):
        if student["brojIndeksa"] == broj_indeksa:
            studenti[i].update(dict(flask.request.form))

            smer = list(filter(lambda s: s["sifra"] == studenti["smer"], studijski_programi))
            if len(smer) > 0:
                studenti[i]["smer"] = smer[0]
            else:
                studenti[i]["smer"] = None

            return flask.redirect("/")
        
    return "Nije pronadjen student za izmenu!", 404


if __name__ == "__main__":
    app.run()