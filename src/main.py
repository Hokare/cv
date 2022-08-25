from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route("/")
def accueil():
    return render_template("accueil.jinja")


@app.route("/competences")
def competences():
    return render_template("competences.jinja")


@app.route("/diplomes")
def diplomes():
    return render_template("diplomes.jinja")


@app.route("/experiences")
def experiences():
    return render_template("experiences.jinja")


@app.route("/Martin-Barbey")
def MartinBarbey():
    return send_file("static/document/Martin-Barbey.pdf")


@app.route("/loisirs")
def loisirs():
    return render_template("loisirs.jinja")


@app.route("/projets")
def projets():
    return render_template("projets.jinja")


@app.route("/scolarite")
def scolarite():
    return render_template("scolarite.jinja")
