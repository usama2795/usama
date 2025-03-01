from flask import Flask

app = Flask(_name_)  # Corrected version

@app.route("/")
def home():
    return "Hello, World!"

if _name_ == "_main_":
    app.run()
