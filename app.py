from flask import Flask

app = Flask(_name_)  # Corrected version

@app.route("/")
def home():
    return "hello,Shaban Qadeer Khan"

if _name_ == "_main_":
    app.run()
