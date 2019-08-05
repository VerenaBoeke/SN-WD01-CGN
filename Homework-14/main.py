from flask import Flask, render_template

app=Flask(__name__)#MODEL

@app.route("/")#CONTROLLER
def index():
    return render_template("index.html")

@app.route("/impressum")#CONTROLLER
def about_me():
    return render_template("impressum.html")

if __name__ == '__main__':
    app.run()