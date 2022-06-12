
from flask import Flask

app=Flask (__name__)

@app.route('/index/')
@app.route("/")
def index():
    return"<h2>This is my IoI web</h2>"

if __name__=='__main__':
    app.run()