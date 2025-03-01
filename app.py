from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return "Hello, my name is butt and this is my app!"

if _name_ == '_main_':
    app.run(debug=True)
