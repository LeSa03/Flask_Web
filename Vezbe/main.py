import flask
from flask import Flask

app = Flask(__name__, static_url_path="/")

studenti = [
    {"brojIndeksa": "1234/123456", "ime": "Marko", "prezime": "Petrovic", "prosecnaOcena": 8.2},
    {"brojIndeksa": "2234/123456", "ime": "Jovan", "prezime": "Jovanovic", "prosecnaOcena": 6.2},
    {"brojIndeksa": "3234/123456", "ime": "Tejodora", "prezime": "markovic", "prosecnaOcena": 9.2},
    {"brojIndeksa": "4234/123456", "ime": "Jovana", "prezime": "Petrovic", "prosecnaOcena": 8.8},
]

@app.route("/")
@app.route("/home")
@app.route("/home.html")
@app.route("/index")
@app.route("/index.html")
def home():
    redovi = ""
    for student in studenti:
         kolone = ""
         for k in student:
             kolone += f"<td>{student[k]}</td>"
         kolone += f'<td><a href="/ukloni?student={student["brojIndeksa"]}">Ukloni</a> <a href="/izmeni?student={student["brojIndeksa"]}">Izmeni</a></td>'
         redovi += f"<tr>{kolone}</tr>\n"

    return f'''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <a href="/forma.html">Forma za dodavanje</a>
    <table>
      <thead>
        <tr>
          <th>Broj indeksa</th>
          <th>ime</th>
          <th>prezime</th>
          <th>Prosecna ocena</th>
          <th>Akcije</th>
        </tr>
      </thead>
      <tbody>
          {redovi}
      </tbody>
    </table>
  </body>
</html>
'''
    #return app.send_static_file("index.html")

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
def forma_za_zimenu():
    broj_indeksa = flask.request.args.get("student")
    for student in studenti:
        if student["brojIndeksa"] == broj_indeksa:
            student_za_izmenu = studnet

    if student_za_izmenu is None:
        return "nije pronadjen", 404
    return '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Forma</title>
  </head>
  <body>
    <form onsubmit="return validacija()" action="/izmeni?student={}" method="post">
      <div>
        <label
          >Broj indeksa
          <input id="broj-indeksa" type="text" name="brojIndeksa" required
        /></label>
      </div>
      <div>
        <label>Ime <input type="text" name="Ime" required /></label>
      </div>
      <div>
        <label>Przime <input type="text" name="Prezime" required /></label>
      </div>
      <div>
        <label
          >Prosecna ocena
          <input
            type="number"
            min="5"
            max="10"
            step="0.01"
            name="prosecnaOcena"
            required
        /></label>
      </div>
      <div>
        <button type="submit">Dodaj</button>
      </div>
    </form>
    <script src="skripta.js"></script>
  </body>
</html>

'''

if __name__ == "__main__":
    app.run()