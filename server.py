from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def display():
    return render_template("index.html")

@app.route('/Joke')
def Joke():
    return '<h2> What did 0 say to 8 <h2/>'

@app.route('/Joke/Punch')
def Punch():
    return '<h2> Nice Belt <h2/>'

if __name__== '__main__':
    app.run(debug = True)
