from flask import Flask

app = Flask(__name__, static_url_path="/")

#@app.route("/style.css")
#def stil():
#    return app.send_static_file("style.css")

@app.route("/")
@app.route("/home")
@app.route("/home.html")
@app.route("/index")
@app.route("/index.html")
def home():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run()