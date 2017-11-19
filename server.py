from flask import Flask, request, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'dev'
app.config['MONGO_URI'] = 'mongodb://guffaw:chuckles@cluster0-shard-00-00-md5j0.mongodb.net:27017,cluster0-shard-00-01-md5j0.mongodb.net:27017,cluster0-shard-00-02-md5j0.mongodb.net:27017/dev?authSource=admin&replicaSet=Cluster0-shard-0&ssl=true'

mongo = PyMongo(app)


@app.route('/')
def display():
    return render_template("index.html")

@app.route('/Joke')
def Joke():
    joke = mongo.db.jokes.find({})
    print(joke.next());
    return '<h2> Joke Page<h2/>'

@app.route('/Joke/Punch')
def Punch():
    return '<h2> Nice Belt <h2/>'

if __name__== '__main__':
    app.run(debug = True)
