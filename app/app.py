from flask import Flask, jsonify, render_template

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# HTML ROUTES
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/model")
def model():
    return render_template("ML.html")  # Ensure you have a corresponding model.html file

@app.route("/dashboard")
def dashboard():
    return render_template("tableau1.html")

@app.route("/battle")
def battle():
    return render_template("tableau2.html")  # Ensure you have a corresponding battle.html file

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/works_cited")
def works_cited():
    return render_template("works_cited.html")


if __name__ == "__main__":
    app.run(debug=True)
