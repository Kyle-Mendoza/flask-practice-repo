from flask import Flask 
from flask import render_template, request, redirect
import os 

app = Flask(__name__)

# set upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ensure the upload folder exists 
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload_file", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if "file" not in request.files:
            return "No File Part"
        
        file = request.files["file"]

        if file.filename == "":
            return "No Select File"
        
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        return f"File {file.filename} uploaded successfully!"

    return render_template('upload_form.html')
    

if __name__ == "__main__":
    app.rub(debug=True)