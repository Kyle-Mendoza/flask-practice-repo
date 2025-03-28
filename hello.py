from flask import Flask, url_for
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



@app.route("/<string:name>")
def escape_test(name):
  return f"Hello, {escape(name)}"



@app.route("/test/<path:testpath>") #<path: > converter accepts / unlike <string: >
def path_test(testpath):
  return f"{testpath}"



with app.test_request_context():
  print(url_for("index"))
  print(url_for("hello_world", next="/"))
  print(url_for("check_member", id=1))
  print(url_for("escape_test", name="Kyle"))
  print(url_for("path_test", testpath="this/is/test/path"))
# url_for(method, params=value)


  
if __name__ == "__main__":
  app.run(debug=True)
