from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
  return "<p>This is the Index Page</p>"



@app.route("/hello")
def hello_world():
  return "<p>Hello, World!</p>"



@app.route("/member/<int:id>")
def check_member(id):
  return f"<p>Hello Member {id}, This is a Test</p>"



@app.route("/<name>")
def escape_test(name):
  return f"Hello, {escape(name)}"



@app.route("/test/<path:testpath>") #<path: > converter accepts / unlike <string: >
def test(testpath):
  return f"{testpath}"





if __name__ == "__main__":
  app.run(debug=True)
