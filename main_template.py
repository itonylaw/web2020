from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    msg = 'My name is TonyDeep'
    return render_template("index.html",data = msg)

if __name__ == "__main__":
    app.run(port = 2020, host="127.0.0.1", debug = True)
