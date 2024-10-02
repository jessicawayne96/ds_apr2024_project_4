from flask import Flask, jsonify, render_template
from SQLHelper import SQLHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sql = SQLHelper()

#################################################
# Flask Routes
#################################################

# HTML ROUTES
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/model")
def model():
    return render_template("model.html")  # Ensure you have a corresponding model.html file

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/battle")
def battle():
    return render_template("battle.html")  # Ensure you have a corresponding battle.html file

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/works_cited")
def works_cited():
    return render_template("works_cited.html")
    
# SQL Queries
@app.route("/api/v1.0/get_dashboard/<gender>/<marital_status>")
def get_dashboard(gender, marital_status):
    data = sql.get_dashboard(gender, marital_status)
    return jsonify(data)

@app.route("/api/v1.0/get_map/<occupation>")
def get_map(occupation):
    data = sql.get_map(occupation)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
