from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/GET")
def get_data():
    return "Succesfully got data.."

if __name__ == "__main__":
    app.run(debug=True)