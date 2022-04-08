from flask import Flask


app = Flask(_ttt_)


@app.route('/')
def index():
    return "Привет, мир!"
    
    
    app.run(port='8000')
