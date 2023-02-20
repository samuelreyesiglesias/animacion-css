#crear aplicacion  python 3.6 usando Flask
#pip install flask
#pip install flask-mysqldb
#pip install flask-cors
#pip install flask-restful
#pip install flask-jwt-extended
#pip install flask-bcrypt
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
#create about page
@app.route("/about")
def about():
    return "The about page"
if __name__ == "__main__":
    app.run()   
#ejecutar en terminal
#python codigo-py.py