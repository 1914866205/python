
from flask import Flask
app = Flask(__name__)
@app.route("/python")
def hello():
    return "PythonApi: Hello World!"
if __name__ == "__main__":
    app.run()
