from flask import Flask ,render_template, request , url_for, redirect
import os

from databaseClass import Db , Note


## Obteniendo el path de la carpeta template
dir_template = os.path.dirname(os.path.abspath(__file__))
dir_template = os.path.join(dir_template,'src','templates')

## Configuracion de la app Flask
app = Flask(__name__, template_folder = dir_template)

db = Db()

@app.route("/", methods = ["GET","POST"])
def main():
    arr = db.getNotas()        
    return render_template("index.html", lista = arr)

@app.route('/addNote', methods = ["POST"])
def addNote():
    title = request.form["title"]
    description = request.form["description"]
    print(f"{title} y {description}")
    if title and description:
        db.insertNote(title,description)

    return redirect(url_for('main'))

@app.route('/delete/<string:id>')
def deleteNote(id):
    db.deleteNote(int(id))
    return redirect(url_for('main'))

@app.route('/updateNote/<string:id>', methods=["POST"])
def updateNote(id):
    title = request.form["title"]
    description = request.form["description"]

    if title and description:
        db.updateNote(title,description,id)

    return redirect(url_for("main"))

if __name__ == '__main__' :
    app.run(debug=True, port=4000)
    db.closeSession()